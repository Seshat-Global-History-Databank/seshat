seshat.apps.core.custom_filters
===============================

.. py:module:: seshat.apps.core.custom_filters


Attributes
----------

.. autoapisummary::

   seshat.apps.core.custom_filters.register


Functions
---------

.. autoapisummary::

   seshat.apps.core.custom_filters.get_attributes
   seshat.apps.core.custom_filters.zip_lists


Module Contents
---------------

.. py:function:: get_attributes(obj)

   A custom filter to get all attributes of an object in a template.

   :param obj: The object to get attributes from.
   :type obj: object

   :returns: A dictionary of the object's attributes.
   :rtype: dict


.. py:function:: zip_lists(a, b)

   A custom filter to zip two lists together in a template.

   :param a: The first list to zip.
   :type a: list
   :param b: The second list to zip.
   :type b: list

   :returns: A zip object of the two lists.
   :rtype: zip


.. py:data:: register

