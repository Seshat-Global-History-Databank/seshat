Database backups
===============

The current process for backing up the Seshat database is as follows:

1. ssh into the server hosting the database e.g. `seshat-db.com` (see `websites <websites.rst>`_):

    .. code-block:: bash

        ssh user@server

2. Create a dumpfile backup of the PostgreSQL database, where `<seshat_db_name>` is the name of the database and `<date>` is the current date:

    .. code-block:: bash

        pg_dump -U postgres -d <seshat_db_name> > backup_<date>.dump

3. Download the dumpfile to your local machine:

    .. code-block:: bash

        scp user@server:/path/to/backup_<date>.dump /path/to/backup_<date>.dump

4. Upload the dumpfile to this `google drive folder <https://drive.google.com/drive/folders/1c5djM48ve91t84Ug4a8JksSC0p4J-eav?usp=sharing>`_.