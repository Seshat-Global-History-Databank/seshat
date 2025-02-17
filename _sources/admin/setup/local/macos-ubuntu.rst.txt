Setting up a local Ubuntu environment on a Mac
==============================================

In this guide, we will walk you through setting up a local Ubuntu environment on a Mac. This guide is intended for software engineers who are working on the Seshat project and need to set up a local development environment.

We will use multipass to create a virtual machine running Ubuntu on your Mac. Multipass is a lightweight VM manager for Linux, Windows, and macOS. It's designed for developers who need a fresh Ubuntu environment with a single command.

Prerequisites
-------------

You will need to have Homebrew installed on your Mac to install multipass. If you need to install Homebrew, you can find instructions on how to do so on `Homebrew's website <https://brew.sh/>`_.

Steps
-----

1. Install multipass with brew:

   .. code-block:: bash

       $ brew install multipass

   - Note: the images used by Multipass don’t have a pre-installed graphical desktop

2. Create a VM (Ubuntu 22.04)

   .. code-block:: bash
        
       $ multipass launch 22.04

   - This should create a VM called `primary` by default

3. Make sure the VM has enough resources:

   .. code-block:: bash

       $ multipass stop primary
       $ multipass set local.primary.cpus=4
       $ multipass set local.primary.disk=60G
       $ multipass set local.primary.memory=8G
       $ multipass start primary

4. Mount the dir containing the database dump to the VM:

   .. code-block:: bash

       $ multipass mount /path/to/database_dumps/ primary:database_dumps

5. Then log in to the VM with `multipass shell` and install pre-requisites:

   .. code-block:: bash

       $ sudo apt update
       $ sudo add-apt-repository ppa:deadsnakes/ppa
       $ sudo apt install python3.8 -y
       $ sudo apt install python3.8-venv -y
       $ sudo apt-get install python3.8-dev -y
       $ sudo apt-get install g++ -y
