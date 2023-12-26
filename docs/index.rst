.. Python Local SnowFlake documentation master file, created by
   sphinx-quickstart on Thu Nov 13 11:58:26 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

============================================
Welcome to Python SnowFlake's documentation!
============================================

A library that provides snowflake features to python, including Client & Server.

This is extend of https://github.com/koblas/pysnowflake with Client adding.

.. _installation:

------------
Installation
------------

    .. code-block:: bash

        pip install pysnowflake

.. _run_server:

----------
Run server
----------

    .. code-block:: bash

        snowflake_start_server [--dc=DC_ID] [--worker=WORKER_ID] [--host=ADDRESS] [--port=PORT] [--num_processes=NUM_PROC]

With configuration default value:

    1. dc (int, 2 bit): be searched in environment `PSF_DC` first, if not found, get the 0 value.
    2. worker (int, 8 bit): be searched in environment `PSF_WORKER` first, if not found, get the 0 value.
    3. address (domain, inet): default is `localhost`.
    4. port (int): default is `8910`.
    5. num_processes (int): default is `1`.

.. _api:

----
APIs
----

All APIs through http `GET` method.

+-------------+---------------------------------------------------+
| API Path    | Description                                       |
+=============+===================================================+
|  **/**      | Get/Generate the ID                               |
+-------------+---------------------------------------------------+
|  **/stats** | Get the information and statistic for this worker |
+-------------+---------------------------------------------------+

.. _how-to-use:

-----------
How to use?
-----------

    .. code-block:: python

        # just import and use it
        import snowflake.client

        # One time only initialization
        >>> snowflake.client.setup(host, port)
        # Then get the ID whenever you need
        >>> snowflake.client.get_guid()
        3631957913783762945
        # See the stats if you want
        >>> snowflake.client.get_stats()
        {
            'dc': 0,
            'worker': 0,
            'timestamp': 1416207853020, # current timestamp for this worker
            'last_timestamp': 1416207845161, # the last timestamp that generated ID on
            'sequence': 12, # the sequence number for last timestamp
            'sequence_overload': 1, # the number of times that the sequence is overflow
            'errors': 1, # the number of times that clock went backward
        }
