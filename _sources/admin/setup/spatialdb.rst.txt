Cliopatria shape dataset
-------------------------

1. Clone the `Cliopatria GitHub repository <https://github.com/Seshat-Global-History-Databank/cliopatria>`_.
2. Unzip the file ``cliopatria.geojson.zip``.
3. Enter the `notebooks` directory and set up the Python environment as per the instructions in the `README.md` file in the same directory.
4. Run the following command to add colours to the dataset:

   .. code-block:: bash

      $ python convert_data.py ../cliopatria.geojson

   This will create a new file with the name "cliopatria_seshat_processed.geojson".
   Note: You can preview the file in the Jupyter notebook found in the `notebooks` directory. Instructions on how to run the notebook are found in the `README.md` file in the same directory.
5. Go back to the Seshat repo on the machine the website code is running from (if you are running it on a remote server, upload the processed GeoJSON). With your Seshat Python environment activated, you can populate ``core_cliopatria`` table using the following command:

   .. code-block:: bash

      $ python manage.py populate_cliopatria /path/to/cliopatria_seshat_processed.geojson


GADM
----

1. `Download <https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip>`_ the whole world GeoPackage file from the `GADM website <https://gadm.org/download_world.html>`_.
2. Populate the ``core_gadmshapefile``, ``core_gadmcountries`` and ``core_gadmprovinces`` tables using the following command:

   .. code-block:: bash

      $ python manage.py populate_gadm /path/to/gpkg_file

How to add new shape datasets to the maps
------------------------------------------

Ensure that the database and Django are already set up (see the relevant `setup <index.rst>`_ page for more detail) and all migrations have been run for the "core" Django app (``python manage.py migrate core``).

To create a new shape dataset for use in the Seshat map explorer, you can do the following:

1. Create a new model for the new dataset in ``seshat/apps/core/models.py``
2. Generate migration from model, and run it for your database to create the table

   .. code-block:: bash

      $ python manage.py makemigrations core
      $ python manage.py migrate core

3. Create a new "command" at `seshat/apps/core/management/commands` which can be used to populate the db table from the dataset files
   - See the examples below
   - Add a new header on this page to document here how this works

4. Create a new view and update the the map template with the necessary logic to use this dataset
   - views at ``seshat/apps/core/views.py``
   - template e.g. ``seshat/apps/core/templates/core/world_map.html``