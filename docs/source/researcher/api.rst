.. _API Getting Started:

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