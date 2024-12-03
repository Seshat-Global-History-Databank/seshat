Setting up Seshat in a local macOS environment
==============================================

Prerequisites
-------------

Seshat requires the following software to be installed on your machine:

- Python 3
- PostgreSQL 16 with PostGIS
- GDAL
- GEOS

.. admonition:: Installation instructions for prerequisites
    :class: dropdown

    **Python 3**

    Ensure you have a working installation of Python 3. The application has been tested with Python **3.8.13**.

    If you don't have Python installed, you can download it from the `official website <https://www.python.org/downloads/>`_.

    **PostgreSQL and PostGIS**

    Ensure you have a working installation of PostgreSQL with PostGIS. The application has been tested with PostgreSQL **16**.

    If you don't have the software installed, you can use the instructions on `Postgres' website <https://postgresapp.com/>`_ to install it on macOS.

    **GDAL and GEOS**

    Ensure you have a working installation of GDAL and GEOS.

    .. hint::

        If you need to install Homebrew, you can find instructions on how to do so on `Homebrew's website <https://brew.sh/>`_.

    If you don't have them, you can install them using Homebrew.

    Then use Homebrew to install ``gdal`` and ``geos``:

    .. code-block:: bash

        $ brew install gdal geos


Step 1: Set up a virtual environment for the project
----------------------------------------------------

You can use either Conda or Python's built-in ``venv`` module to create a virtual environment for the project.

.. tabs::

   .. tab:: Conda example

      Create the environment:

      .. code-block:: bash

         $ conda create --name seshat python=3.8.13

      Activate the environment:

      .. code-block:: bash

         $ conda activate seshat

   .. tab:: venv example

      Create the environment:

      .. code-block:: bash

         $ python3.8 -m venv seshat

      Activate the environment:

      .. code-block:: bash

         $ source seshat/bin/activate

Step 2: Clone the repo
----------------------

Using your Terminal, clone the repository:

.. code-block:: bash

    $ git clone https://github.com/Seshat-Global-History-Databank/seshat


Step 3: Create an empty database and add the PostGIS extension
--------------------------------------------------------------

.. hint::

    Note that you'll have to use ``;`` to end each SQL command. They will not work without this character.

In order to create a database, open ``psql`` in the terminal:

.. code-block:: bash

    $ psql postgres

In the database, run the following SQL command to create a new database. Note that you should replace ``<seshat_db_name>`` with the name you want to give the database:

.. code-block:: sql

    CREATE DATABASE <seshat_db_name>;

Exit out of the ``psql`` program:

.. code-block::

    \q

Then open the database using the name you just created in place of ``<seshat_db_name>``:

.. code-block:: bash

    $ psql postgres -d <seshat_db_name>

Now, you can add the PostGIS extension to your database:

.. code-block:: sql

    CREATE EXTENSION postgis;


Step 4: Configure GDAL and GEOS
-------------------------------

.. hint::

    Note: If you installed GDAL and GEOS using Homebrew, you can find the paths to the installations by running ``brew info gdal`` and ``brew info geos``.

    The paths should look something like ``/opt/homebrew/Cellar/gdal/3.9.0_1`` and ``/opt/homebrew/Cellar/geos/3.9.1``.

Open :doc:`seshat/settings/base.py </api/seshat/settings/base/index>` and check (or update) the paths in the following variables, which should be to the paths to your local ``gdal`` and ``geos`` installations:

- ``GDAL_LIBRARY_PATH``
- ``GEOS_LIBRARY_PATH``

Note: there are hardcoded paths in ``base.py`` for the Mac and Ubuntu instructions above included.


Step 5: Install the Python packages
-----------------------------------

Install the Python packages in your environment (some packages have these as dependencies).

From the top level of the ``seshat`` directory, run the following commands to install the packages from the ``requirements.txt`` file and the ``django-geojson`` package:

.. code-block:: bash

    $ pip install -r requirements.txt
    $ pip install "django-geojson [field]"


Step 6: Seshat database setup
-----------------------------

Restore Seshat database from dump file:

.. code-block:: bash

    $ pg_restore -U postgres -d <seshat_db_name> /path/to/file.dump


Step 7: Secure the database
---------------------------

Add a password to the database for security.

Add a password for the superuser by logging in to the database with your superuser:

.. code-block:: bash

    $ psql -U postgres

Send the following SQL command to set the password for the superuser. Make sure to replace ``<db_password>`` with your desired password (and make sure to remember it):

.. code-block:: sql

    ALTER USER postgres WITH PASSWORD '<db_password>';

Locate ``pg_hba.conf`` if you don't know where it is

.. code-block:: bash

    $ psql -U postgres -c 'SHOW hba_file;'

Update postgres to use md5 with ``nano /path/to/pg_hba.conf``

.. image:: ../../../img/pg_hba.conf.png


Step 8: Set up environment variables for connecting to the database
-------------------------------------------------------------------

Create a configuration file with your database info for Django. The presence of this file will ensure Django connects to your local database.

Within the repo, create a file called ``seshat/settings/.env`` with the database connection variables.

.. admonition:: Get a Cesium access token
    :class: dropdown

    You will also need to generate an access token for Cesium in order for the globe to render on Seshat pages that include maps.

    Visit the `Cesium website <https://ion.cesium.com/>`_ and create an account.

    Once you have an account, navigate to the "Access Tokens" tab and create a new token.

    Add this token to the ``.env`` file as shown below.

The file should look like this:

.. code-block::

    DB_NAME=<seshat_db_name>
    DB_USER=postgres
    DB_HOST=localhost
    DB_PORT=5432
    DB_PASSWORD=<db_password>
    CESIUM_ION_ACCESS=<cesium_access_token>


Step 9: Migrate the database
-----------------------------

Ensure that all Django database migrations have run:

.. code-block:: bash

    $ python manage.py migrate

Step 10: Collect static files
-----------------------------

.. code-block:: bash

    $ python manage.py collectstatic


Step 11: Load the shape data
----------------------------

If the shape data tables are not yet populated in your copy of the Seshat core database and you have access to source data, populate one or more of them with the instructions `here <../spatialdb.rst>`_.


Step 12: Run Django
-------------------

.. code-block:: bash

    $ python manage.py runserver

The webapp should be visible in a browser at http://127.0.0.1:8000/
