# Python SnowFlake

A library that provides snowflake features to python, including Client and Server. 

This is extend of https://github.com/koblas/pysnowflake with Client adding.


### Installation

```shell
cd pysnowflake
pip install .
```


### Run Server 

```shell
snowflake_start_server [--dc=DC_ID] [--worker=WORKER_ID] [--address=ADDRESS] [--port=PORT] [--num_processes=NUM_PROC]
```
or
```shell
python -m snowflake.server [--dc=DC_ID] [--worker=WORKER_ID] [--address=ADDRESS] [--port=PORT] [--num_processes=NUM_PROC]
```
With configuration default value:
1. `dc` (int, 2 bit): be searched in environment PSF_DC first, if not found, get the 0 value.
1. `worker` (int, 8 bit): be searched in environment PSF_WORKER first, if not found, get the 0 value.
1. `address` (domain, inet): default is localhost.
1. `port` (int): default is 8910.
1. `num_processes` (int): default is 1.


### APIs

All APIs through http GET method.

1. `/`: Get/Generate the ID
1. `/stats`: Get the information and statistic for this worker


### Run Client

```shell
import snowflake.client

# One time only initialization
snowflake.client.setup(host, port)

# Then get the ID whenever you need
snowflake.client.get_guid()

# See the stats if you want
snowflake.client.get_stats()
```


### Change log

#### 0.1.3

* Fix syntax errors with python 2.7
