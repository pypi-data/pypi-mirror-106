PyMultition
================

|pypi| |license|

A Multiton Class for preventing duplicate instances based on serializing init values.

-  Free software: MIT license

Features
--------

-  Return the same instance if instanciate class with same init value

Quickstart
----------
.. code-block:: python

    from PyMultition import MultitionInstanceFactory
    
    
    class Test:
        def __init__(self, attr):
            self.attr = attr
    
    
    a = MultitionInstanceFactory.get_instance(Test, '1')
    b = MultitionInstanceFactory.get_instance(Test, '2')
    c = MultitionInstanceFactory.get_instance(Test, '2', multition_key='')
    d = MultitionInstanceFactory.get_instance(Test, '2', multition_key='normal')
    e = MultitionInstanceFactory.get_instance(Test, '2', multition_key='special')
    f = MultitionInstanceFactory.get_instance(Test, '2', multition_key='special')
    
    assert a is not b
    assert b is c
    assert c is not d
    assert d is not e
    assert e is f

.. |pypi| image:: https://img.shields.io/pypi/v/PyMultition.svg
   :target: https://pypi.python.org/pypi/PyMultition
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg