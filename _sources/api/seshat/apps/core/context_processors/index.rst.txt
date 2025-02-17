seshat.apps.core.context_processors
===================================

.. py:module:: seshat.apps.core.context_processors


Functions
---------

.. autoapisummary::

   seshat.apps.core.context_processors.notifications


Module Contents
---------------

.. py:function:: notifications(request)

   Handle the notifications logic for authenticated users and fetch necessary
   data.

   :param request: The HTTP request object.
   :type request: HttpRequest

   :returns:

             A dictionary containing:
                 - 'notifications_count' (int): The number of private comments for
                   the authenticated user.
                 - 'all_polities' (QuerySet): A queryset of all polities.
                 - 'search_term' (str): The search term submitted in the request,
                   if any.
   :rtype: dict


