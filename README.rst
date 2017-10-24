demo-dependency
===============

An HTTP API that changes unpredictably!

Usage
-----

*Note that Docker is a prerequisite*

.. code-block:: bash

    $ docker run -d -p 4000:4000 jdgillespie91/demo-dependency:latest
    $ curl localhost:4000
    "Hello, world!"

Development
-----------

Build the image with

.. code-block:: bash

    $ docker build -t demo-dependency:latest .

Run the container with

.. code-block:: bash

    $ docker run -d -p 4000:4000 demo-dependency:latest

Make a call to the application with

.. code-block:: bash

    $ curl localhost:4000
    "Hello, world!"

Deployment
----------

Build the image with

.. code-block:: bash

    $ docker build -t jdgillespie91/demo-dependency:latest .

Push the image with

.. code-block:: bash

    $ docker push jdgillespie91/demo-dependency:latest

