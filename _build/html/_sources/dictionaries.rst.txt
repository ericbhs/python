============
Dictionaries
============

.. contents:: :local:

Creating an empty dictionary
============================

``my_dict = dict()``

or

``my_dict = {}``

Creating a dictionary with content
==================================

``cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}``

=> ``{key:value, key:value...}``

Adding an item to a dictionary
==============================

.. code-block :: python

	>>> my_dict = {}
	>>> my_dict["login"] = "eric"
	>>> my_dict["password"] = "azerty"
	>>> my_dict
	{'password': 'azerty', 'login': 'eric'}
	
Access a specific item
======================

.. code-block :: python

	>>> my_dict["password"]
	"azerty"
	
Delete an item
==============

``del`` keyword
---------------

.. code-block :: python

	>>> cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}
	>>> cupboard
	{'shirts': 3, 'trousers': 6, 'tee-shirts': 7}
	>>> del cupboard['shirts']
	>>> cupboard
	{'trousers': 6, 'tee-shirts': 7}


``pop()`` method
----------------

**Returns** a value from the dictionary and **removes** the corresponding key

.. code-block :: python

	>>> cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}
	>>> cupboard
	{'shirts': 3, 'trousers': 6, 'tee-shirts': 7}
	>>> cupboard.pop('trousers')
	6
	>>> cupboard
	{'shirts': 3, 'tee-shirts': 7}
	>>> cupboard.pop('shirts')
	3
	>>> cupboard
	{'tee-shirts': 7}
	>>> cupboard.pop('tee-shirts')
	7
	>>> cupboard
	{}

Dictionaries to store functions
===============================

.. code-block :: python

	def hello():
		print("Hello everyone !")

	def bird():
		print("Chirp chirp !")
		
	functions_dict = {}
	functions_dict["hello"] = hello # Reference to function -> no parenthesis
	functions_dict["bird"] = bird

	functions_dict["hello"]() 	# Returns "Hello everyone !"
	functions_dict["bird"]() 	# Returns "Chirp chirp !"

Iterate on keys
===============

**Note : dictionaries are not ordered, so the iteration might not return the keys/values entered the same way we entered them**

Implicit
--------

.. code-block :: python

	cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}

	for k in cupboard:
		print(k)
		
Returns :

.. code-block :: python

	shirts
	trousers
	tee-shirts
	
Explicit
--------

Use ``keys()`` method to be more explicit (recommended ; exact same thing as the implicit one) :

.. code-block :: python

	cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}

	for k in cupboard:
		print(k)
		
Returns :

.. code-block :: python

	shirts
	trousers
	tee-shirts
	
Iterate on values
=================

.. code-block :: python

	cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}

	for v in cupboard.values():
		print(v)
		
Returns :

.. code-block :: python

	3
	6
	7

Iterate on keys and values simultaneously
=========================================

Works the same way as ``enumerate()`` for lists

.. code-block :: python

	cupboard = {"shirts":3, "trousers":6, "tee-shirts":7}

	for k,v in cupboard.items():
		print("key :", k, "; value :", v)
		
Returns :

.. code-block :: python

	key : shirts ; value : 3
	key : trousers ; value : 6
	key : tee-shirts ; value : 7
	
Transform keys / values into a list of keys / values
====================================================

``dict.values()`` returns a ``dict_values`` object, and ``dict.keys()`` returns a ``dict_keys`` object. Those classes do not allow direct access to its values the list way ``list[i]``. To do so we need to transform them into lists :

.. code-block :: python

	list(cupboard.keys())
	list(cupboard.values())
	
Dictionaries and function parameters
====================================

Use the named parameters as a dictionary inside the function
------------------------------------------------------------

We define a function that takes named parameters the following way :

.. code-block :: python

	def my_function(**named_params):
		...
		
We call this function the following way :

.. code-block :: python

	my_function(param1=x, param2=y...)

We can access those parameters in the function as a dictionaru :

.. code-block :: python

	def my_function(**named_params):
		...
		named_params['param1']
		named_params['param2']
		
Call a function with named parameters with a dictionary as parameter
--------------------------------------------------------------------

Example with ``print()`` :

.. code-block :: python

	params = {"sep":" >> ", "end":" -\n"}
	print("Here", "is", "an", "example", **params)

Returns :

.. code-block :: none

	Here >> is >> an >> example -
	
This is the same as calling the ``print()`` function the classic way :

.. code-block :: python

	print("Here", "is", "an", "example", sep=" >> ", end=" -\n")