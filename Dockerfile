FROM postgis/postgis

# Update the package lists for upgrades for packages that need upgrading, as well as new packages that have just come to the repositories.
RUN apt-get update -y

# Install the packages
RUN apt-get install -y gdal-bin libgdal-dev libgeos++-dev libgeos-c1v5 libgeos-dev libgeos-doc

# Install pip
RUN apt-get install -y python3-pip

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy requirements.txt file into the Docker image
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Install django-geojson
RUN pip install "django-geojson[field]"