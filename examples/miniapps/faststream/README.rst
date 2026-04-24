FastStream + Dependency Injector Example
========================================

This is a `FastStream <https://github.com/ag2ai/faststream>`_ +
`Dependency Injector <https://python-dependency-injector.ets-labs.org/>`_ example application.

The example application is a simple consumer that counts messages sent to redis channel by producer.

Counter is provided to faststream handler as a dependency injected by ``dependency_injector`` library.

Run
---

Everything can be run via docker compose.

A convenient ``run.sh`` script runs consumer, producer and redis services, prints logs from consumer
and shuts down once producer exits.


Run the sciprt:

.. code-block:: bash

    ./run.sh

The output should be something like:

.. code-block::

    faststream-example-consumer  | Message #1 from John: 'As you can see'
    faststream-example-consumer  | Message #2 from John: 'messages are counted correctly'
    faststream-example-consumer  | Message #3 from John: 'by the counter that is injected'
    faststream-example-consumer  | Message #4 from John: 'into faststream handler'
    faststream-example-consumer  | Message #5 from John: 'via awesome dependency_injector library.'


Once you've done working with this example you can clean up docker images and containers it produced:

.. code-block:: bash

    docker compose down --rmi local
