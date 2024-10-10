Getting started with Seshat data
=================================

This section of the documentation provides information on how to get started with accessing Seshat data as a researcher, both through the Seshat website and the Seshat API, as well as the Cliopatria borders GeoJSON dataset.

Creating a login on the Seshat website
---------------------------------------

Creating an account on the Seshat website is the first step to accessing the Seshat data. You can do this by visiting the `Seshat website <https://seshat-db.com/>`_ and clicking the "Sign up" button in the top right corner.

Follow the information on the screen to create your account.

Loading Seshat data in Python via the Seshat API
------------------------------------------------

You can access (and download) the latest Seshat data from the website using the Seshat API (Application Programming Interface).
The advantage of the API is that it allows you to access up-to-date Seshat data *programmatically*, allowing you to work with this data on your computer in a programming language such as Python.

The best way to get started with loading data via the Seshat API is to use our Python package, which is available at `github.com/Seshat-Global-History-Databank/seshat_api <https://github.com/Seshat-Global-History-Databank/seshat_api>`_.
If using the API for the first time, open the `examples` folder in the repository where you can find Jupyter notebooks that demonstrate how to use the API to load data in Python.
The README file in the `examples` folder provides instructions on how to install the package and run the examples.

.. tip::

   You may want to start by reading the `Software tools <software-tools>`_ page to ensure you have Python and Git installed on your computer.


.. note::

    - The Seshat API is a RESTful API that allows you to query the Seshat database and retrieve data in JSON format.
    - It is available on the Seshat website at `seshat-db.com/api <https://seshat-db.com/api/>`_. 
    - Loading the API in your browser will show you the available endpoints and the data that can be retrieved from them.
    - There is a filter option that allows you to specify the data you want to retrieve from the API.

Working with the Cliopatria borders dataset
--------------------------------------------

The Cliopatria borders dataset is available as part of the Seshat database and API. It is used on the `World Map <https://seshat-db.com/core/world_map>`_ and polity pages of the Seshat website.

Cliopatria is also available as a stand-alone dataset which is stored and documented at `github.com/Seshat-Global-History-Databank/cliopatria <https://github.com/Seshat-Global-History-Databank/cliopatria>`_.
The data takes the form of a single GeoJSON file, a format that can be loaded by a wide variety of software for handling geospatial data.

A great way to get started exploring the Cliopatria dataset is to open it in the Jupyter notebook example found inside the `github.com/Seshat-Global-History-Databank/cliopatria <https://github.com/Seshat-Global-History-Databank/cliopatria>`_ GitHub repo.
The `notebooks` folder contains a processing script to add colors to the dataset, alongside a notebook which loads the data in GeoPandas and includes an interactive Folium plot.
Follow the README instructions in the `notebooks` folder.

.. tip::

    You may want to start by reading the `Software tools <software-tools>`_ page to ensure you have Python and Git installed on your computer.