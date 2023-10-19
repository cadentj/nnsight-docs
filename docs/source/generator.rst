Generator
=========

Now calling .generate(...) does not actually initialize or run the model. Only after the with 
generator block is exited, is the acually model loaded and ran. 
All operations in the block are "proxies" which essentially 
creates a graph of operations we wish to carry out later.

Generate Context
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. .. py:function:: lumache.get_random_ingredients(kind=None)

..    Return a list of random ingredients as strings.

..    :param kind: Optional "kind" of ingredients.
..    :type kind: list[str] or None
..    :raise lumache.InvalidKindError: If the kind is invalid.
..    :return: The ingredients list.
..    :rtype: list[str]


.. automodule:: engine.contexts.Generator
   :members:

