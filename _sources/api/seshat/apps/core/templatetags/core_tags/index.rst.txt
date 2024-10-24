seshat.apps.core.templatetags.core_tags
=======================================

.. py:module:: seshat.apps.core.templatetags.core_tags


Attributes
----------

.. autoapisummary::

   seshat.apps.core.templatetags.core_tags.register


Functions
---------

.. autoapisummary::

   seshat.apps.core.templatetags.core_tags.get_polity_capitals
   seshat.apps.core.templatetags.core_tags.polity_map


Module Contents
---------------

.. py:function:: get_polity_capitals(pk)

   Get all the capitals for a polity and coordinates.

   :param pk: The primary key of the polity.
   :type pk: int

   :returns:

             A list of dictionaries containing the capital name, latitude,
                 longitude, start year (or 0 or None if they aren't present in the
                 database), and end year (or 0 or None if they aren't present in
                 the database).
   :rtype: list


.. py:function:: polity_map(pk, test=False)

   This function is used by the polity_map template and gets the specific
   polity shape data and capital information. Sets include_polity_map to False
   if there is no shape data. include_polity_map is used to determine whether
   to display the map on polity_detail.html.

   :param pk: The primary key of the polity.
   :type pk: int

   :returns:

             The content dictionary containing the polity shape data and
                 capital information.
   :rtype: dict


.. py:data:: register

