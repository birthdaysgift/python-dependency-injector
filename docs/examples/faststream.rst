.. _faststream-example:

FastStream example
=============

.. meta::
   :keywords: Python,Dependency Injection,FastStream,Example
   :description: This example demonstrates a usage of FastStream with Dependency Injector.


This example shows how to use ``Dependency Injector`` with `FastStream <https://github.com/ag2ai/faststream>`_.

The source code is available on the `Github <https://github.com/ets-labs/python-dependency-injector/tree/master/examples/miniapps/faststream>`_.

Despite ``FastStream`` uses ``FastDepends`` library for dependency injection, the integration between
``Dependency injector`` and ``FastStream`` has a small difference from already existing :ref:`fastdepends` example.

Since ``FastStream`` also leverages function signatures to determine input data types you have to use ``Depends()`` function
with ``cast=False`` argument to make ``FastStream`` ignore your injected dependency argument in the function signature.

Example below shows how to inject ``Counter`` class into ``FastStream`` redis handler so that it will distinguish between
message schema (``User``) and injected dependency (``Counter``) and use them both correctly.

Listing of ``consumer.py``:

.. literalinclude:: ../../examples/miniapps/faststream/src/consumer.py
   :language: python

Listing of ``producer.py``:

.. literalinclude:: ../../examples/miniapps/faststream/src/producer.py
   :language: python

Sources
-------

Explore the sources on the `Github <https://github.com/ets-labs/python-dependency-injector/tree/master/examples/miniapps/faststream>`_.

.. include:: ../sponsor.rst

.. disqus::

