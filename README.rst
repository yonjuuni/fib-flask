======================
Fibonacci sequence API
======================
This is a simple implementation of HTTP API on Flask.

Usage
-----

``GET {hostname}/v1/fib/{int}`` - get sequnce for a provided integer.
Supports integers in range from 0 to 1000.

Example request:
~~~~~~~~~~~~~~~~
``$ curl http://localhost:5000/v1/fib/10``

Example response:
~~~~~~~~~~~~~~~~~
.. code-block:: json

    {
      "sequence": [
        0, 
        1, 
        1, 
        2, 
        3, 
        5, 
        8, 
        13, 
        21, 
        34, 
        55
      ]
    }

Errors
------
* The number should be in range from 0 to 1000.
* Not an integer.
* Invalid API call.

Implementation / Deployment
---------------------------
Written on Flask.
Test instance deployed at http://api.s1ck.org:12346 using uWSGI + Nginx.


Author
------

`Alex Sanchez <mailto:alex@s1ck.org>`_.
