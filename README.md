python-wykopapi - Pythonic Wykop API
=====================================

**python-wykopapi** is pythonic way to access to Wykop API. Carefully designed to give you easy access to all API
functionality. You can also use low-level API.

Build using requests library and [TDD](http://en.wikipedia.org/wiki/Test-driven_development)

Using High-Level API
--------------------
As mentioned before **python-wykopapi** contain High-level API designed to access any data from Wykop.pl
Let's look at it::

    from wykopapi import Wykop, APIData as A

    api = Wykop('API Key', 'API Secret')

    page = 2

    promoted = api.links.promoted[page](A(sort='day'))
