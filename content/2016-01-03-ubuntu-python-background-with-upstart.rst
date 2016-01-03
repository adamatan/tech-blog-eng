Python background processes in Ubuntu
#####################################

:date: 2016-01-03 10:20
:tags: Ubuntu, Python, Upstart, Tutorial, nohup
:category: yeah
:authors: Adam Matan
:summary: Running and monitoring background Python processes in Ubuntu.

Introduction
------------
Running a process in the background is a very useful technique in software development in the Linux world. Such processes are used in a wide variety of scenarios, ranging from event processing through network polling to system monitoring.

**Common use cases might be:**

- Consuming message from a queue
- Making periodic HTTP calls to a site for monitoing purposes

- For example, one might want to make an HTTP GET call to a resource every minute and send an email notification in case of inavailability, or log the system memory or disk usage every now and

The Easy Solution - ``nohup``
-----------------------------

The Interactive Solution - ``screen``
-------------------------------------

The Robust Solution - ``upstart``
---------------------------------


Best practices
--------------

Virtual environments
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd ~
   virtualenv background_process_env
   source background_process_env/bin/activate


Monitoring
~~~~~~~~~~

Logging
~~~~~~~
