.. Python Local SnowFlake documentation master file, created by
   sphinx-quickstart on Thu Nov 13 11:58:26 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python Local SnowFlake's documentation!
==================================================

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

How does it build Unique ID?
----------------------------

I have referenced the algorithm from:

  1. `Twitter’s Snowflake <http://github.com/twitter/snowflake/>`_
  2. `Facebook Instagram <http://instagram-engineering.tumblr.com/post/10853187575/sharding-ids-at-instagram>`_

to build this library.

The main idea is, each ID is built from 3 parts:

  1. The timestamp part: 41 bit (gives us 41 years of IDs with a custom epoch)
  2. The logical shard part: 15 bit (gives us 128*256 logical shards)
  3. Auto-incrementing sequence part: 8 bit (so we can generates 256 IDs per shard per millisecond)

How does it detect logical shard?
---------------------------------

The idea is: each logical shard is a combination of the server/node and the thread where the code run in.

### Server/Node ID

This is the number to identify the server/node, this will get from environment
variable named: **PYLOCALFLAKE_NODE_ID**

It will take 7 bits, gives us capacity to handle 128 nodes.

### Thread ID

This will identify each thread/instance of the ID generator pernode. This will be
an anto-increment number that be shared all over the server/node.

It will takes 8 bits, give uses capacity to handle 256 threads per node.

I used a file to share this: /tmp/pylocalflake.tid.

This file is a simple database (CSV formatted). Each row has 3 fields in order:
*thread_id, real_process_id, real_thread_id*.

Whenever a localflake instance is created, it will check this file with a lock,
take a comfortable thread-id, save its information (real process-id, real thread-id)
to claim its thread-id, then release the lock.

Whenever a localflake instance is deleted or the process exit, it unclaims the thread-id.
