======================
Conditional structures
======================

Example :

.. code-block:: python
    
    if year % 400 == 0:
        bissextile = True
    elif year % 100 == 0:
        bissextile = False
    elif year % 4 == 0:
        bissextile = True
    else:
        bissextile = False

=============== ===================================
Operator        Litteral meaning
=============== ===================================
<               Strictly less than
>               Strictly greater than
<=              Greater than or equal to
>=              Less than or equal to
==              Equals to
!=              Different than
True            bool "true"
False           bool "false"
and             bool "and"
or              bool "or"
not             bool "not"
=============== ===================================