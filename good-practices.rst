==============
Good practices
==============

PEP = Python Enhancement Proposal

.. image:: _static/naming_recommend.png
    :target: _static/naming_recommend.png

Conventions de nommage
----------------------

Noms à éviter
"""""""""""""

Never use those characters alone as variable names :

* ``l`` (``L`` lowercase)
* ``O`` (``o`` capital)
* ``I`` (``i`` capital).

The display of those caracters with  some fonts might lead to mix them up with ``0`` or ``1``.

Modules and packages names
""""""""""""""""""""""""""

Package : ``package``

Module : ``module_name``

* short names 
* only lowercase characters
* may contain underscores ``_``
* Though packages names may also contain underscores ``_`` but PEP8 does not recommend it.

Classes names
"""""""""""""
``MyClass``

With barely no exception, classes names are made of lowercase letters, with the exception of the first letter of each words that constitutes it.

Exceptions names
"""""""""""""""""

``CustomError``

As exceptions are classe, they are names according to the same convention. If the exception is an error, they integrate the ``Error`` suffix (`SyntaxError``, ``IndexError``, ...)

Variables, object instances, functions and methods
""""""""""""""""""""""""""""""""""""""""""""""""""

``function_name``

``variable_name``

Those use all the same convention : lowercase letters with words separated by underscores ``_``.

Non public methods and instances variables
""""""""""""""""""""""""""""""""""""""""""

``_non_public_method``

``_instance_variable``

Private variables
"""""""""""""""""

``__my_private_variable``

This isn't exactly a convention as it has an impact on the way the interpreter works : it actually replaces the names with ``_ClassName`` prefix. See `here <https://python-cheat-sheet.readthedocs.io/en/latest/classes.html#private-variables>`_ for further infos.

Constants
"""""""""

``NAME_OF_MY_CONSTANT``

All capital letters, with words separated by underscores ``_``.