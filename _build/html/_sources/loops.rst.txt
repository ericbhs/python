=====
Loops
=====

.. contents:: :local:

``while``
---------

.. code-block:: python
    
    while i < 10:
        print("i =", i)

With ``break`` and ``continue`` :

.. code-block:: python

    while True:
        do_something()
        if condition:  
            break
        else:
            continue
        
``for``
-------

Equivalent to ``foreach`` in C#

.. code-block:: python
    
    myList = [1, 2, 3]
    
    for i in myList:
        print(i)
        
``for`` "C-Style"
-----------------

* With ``range()``

.. code-block:: python

    list = [0, 5, 4, 3, 5]
    
    # for (int i=0; i<length(list); i++)
    for i in range(len(list)):
        print("list element", i, "is :", list[i])
        
.. code-block:: python

    list = [0, 5, 4, 3, 5]
    
    # for (int i=a; i>n; i+=s)
    for i in range(a, n, s):
        print("list element", i, "is :", list[i])
        
* With ``Enumerate()`` : returns a list of coupled values containing the list index with its associated element

Example :

.. code-block:: python

    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    for i, elt in enumerate(my_list):
        print("At index", i, "is", elt)
        
-> output :
      
    .. code-block:: none

        At index 0 is a.
        At index 1 is b.
        At index 2 is c.
        At index 3 is d.
        At index 4 is e.
        At index 5 is f.
        At index 6 is g.
        At index 7 is h.