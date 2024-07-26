Setting up new shape datasets
=============================

Ensure that the database and Django are already set up (see :doc:`local instructions </getting-started/setup/local/index>` for more detail) and all migrations have been run for the "core" Django app (``python manage.py migrate core``).

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

Cliopatria shape dataset
-------------------------

..
    TODO: Add a link here to the published Cliopatria dataset

1. Download and unzip the Cliopatria dataset.
2. Update the Cliopatria GeoJSON file with colours and other properties required by Seshat:
   
   .. code-block:: bash

      $ python cliopatria/convert_data.py /path/to/cliopatria.geojson

   Note: this will create a new file with the same name but with the suffix "_seshat_processed.geojson"
3. Populate ``core_cliopatria`` table using the following command:

   .. code-block:: bash

      $ python manage.py populate_cliopatria /path/to/cliopatria_seshat_processed.geojson


GADM
----

1. `Download <https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip>`_ the whole world GeoPackage file from the `GADM website <https://gadm.org/download_world.html>`_.
2. Populate the ``core_gadmshapefile``, ``core_gadmcountries`` and ``core_gadmprovinces`` tables using the following command:

   .. code-block:: bash

      $ python manage.py populate_gadm /path/to/gpkg_file
