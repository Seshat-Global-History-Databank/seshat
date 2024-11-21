import base64
import pulumi
import subprocess
from os.path import expanduser
from pulumi_azure import core, compute, network

# Create an Azure Resource Group
resource_group = core.ResourceGroup('seshat-pulumi', location='uksouth')

# Create a network with a single subnet
virtual_network = network.VirtualNetwork('virtualNetwork',
    resource_group_name=resource_group.name,
    address_spaces=['10.0.0.0/16'],
    subnets=[{
        'name': 'default',
        'address_prefix': '10.0.1.0/24',
    }]
)

# Create a public IP
public_ip = network.PublicIp('publicIp',
    resource_group_name=resource_group.name,
    location=resource_group.location,
    allocation_method='Dynamic',
)

# Create a network security group
network_security_group = network.NetworkSecurityGroup('networkSecurityGroup',
    resource_group_name=resource_group.name,
    security_rules=[
        {'name': 'ssh', 'priority': 1001, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '22', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
        {'name': 'http', 'priority': 1002, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '80', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
        {'name': 'https', 'priority': 1003, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '443', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
        {'name': 'django', 'priority': 1004, 'direction': 'Inbound',
         'access': 'Allow', 'protocol': 'Tcp', 'source_port_range': '*',
         'destination_port_range': '8000', 'source_address_prefix': '*',
         'destination_address_prefix': '*'},
    ]
)

# Associate the network security group with the subnet
association = network.SubnetNetworkSecurityGroupAssociation('association',
    subnet_id=virtual_network.subnets[0].id,  # Use the subnet from the virtual network
    network_security_group_id=network_security_group.id,
)

# Create a network interface and associate it with the subnet
network_interface = network.NetworkInterface('networkInterface',
    resource_group_name=resource_group.name,
    ip_configurations=[{
        'name': 'webserver',
        'subnet_id': virtual_network.subnets[0].id,  # Use the subnet from the virtual network
        'private_ip_address_allocation': 'Dynamic',
        'public_ip_address_id': public_ip.id,
    }]
)

# Get the IP address as a string
# TODO: move this into the VM script and run in python
# ip_address = public_ip.ip_address.apply(lambda ip: ip if ip is not None else '')
# os.environ['ALLOWED_HOSTS'] = ip_address

# Create a data script for the VM
# TODO: Set the ALLOWED_HOSTS environment variable (used by Django)
custom_data_script = '''#!/bin/bash

# Install Python 3.8
sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.8
sudo apt install -y python3.8-venv
sudo apt-get install -y python3.8-dev
sudo apt-get install -y g++

# Install PostgreSQL 16
sudo apt install -y gnupg2 wget vim
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
sudo apt update
sudo apt install -y postgresql-16 postgresql-contrib-16 postgresql-16-postgis-3 
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Install Nginx
sudo apt install -y nginx

# Install GDAL and GEOS
sudo apt-get install -y gdal-bin
sudo apt-get install -y libgdal-dev
sudo apt install -y libgeos++-dev libgeos3.10.2
sudo apt install -y libgeos-c1v5 libgeos-dev libgeos-doc

# Clone Seshat
git clone https://github.com/Seshat-Global-History-Databank/seshat /home/webadmin/seshat
cd /home/webadmin/seshat
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install "django-geojson [field]"


## TODO: Get the pulumi script to run the full setup
# # Create .env file with database configuration
# echo "NAME=<seshat_db_name>
# USER=postgres
# HOST=localhost
# PORT=5432
# PASSWORD=<db_password>" > /home/webadmin/seshat/seshat/settings/.env

# # Run django
# export DJANGO_SETTINGS_MODULE=seshat.settings.local
# gunicorn seshat.wsgi:application --config gunicorn.conf.py &
'''

# Create a VM
vm = compute.LinuxVirtualMachine('vm',
    resource_group_name=resource_group.name,
    network_interface_ids=[network_interface.id],
    size='Standard_D2s_v3',
    source_image_reference={
        'publisher': 'Canonical',
        'offer': '0001-com-ubuntu-server-jammy',
        'sku': '22_04-lts',
        'version': 'latest',
    },
    os_disk={
        'caching': 'ReadWrite',
        'storage_account_type': 'Premium_LRS',
    },
    computer_name='webserver',
    admin_username='webadmin',
    disable_password_authentication=True,
    admin_ssh_keys=[{
        'username': 'webadmin',
        'public_key': pulumi.Config().require_secret('sshPublicKey'),
    }],
    custom_data=base64.b64encode(custom_data_script.encode('ascii')).decode('ascii'),
)

# Export the public IP address of the VM
pulumi.export('publicIp', public_ip.ip_address)

## TODO: Get the pulumi script to run the full setup
# # Create a config object
# config = pulumi.Config()

# # Get the dump file path from the config
# dump_file = config.require('dumpFile')

# # Get the private key path from the config
# private_key_path = expanduser(config.require('privateKey'))

# # Copy database dump file to the VM
# cmd = pulumi.Output.all(private_key_path, dump_file, public_ip.ip_address).apply(
#     lambda args: f"scp -i {args[0]} {args[1]} webadmin@{args[2]}:~/seshat.dump"
# )
# cmd_result = cmd.apply(lambda cmd: subprocess.run(cmd, shell=True, check=True))
