seshat.apps.core.signals
========================

.. py:module:: seshat.apps.core.signals


Functions
---------

.. autoapisummary::

   seshat.apps.core.signals.update_subcomment_ordering


Module Contents
---------------

.. py:function:: update_subcomment_ordering(sender, instance, **kwargs)

   A signal to update the ordering of subcomments when a new subcomment is
   created or an existing subcomment is updated.

   :param sender: The sender of the signal.
   :type sender: SeshatCommentPart
   :param instance: The instance of the subcomment.
   :type instance: SeshatCommentPart
   :param \*\*kwargs: Arbitrary keyword arguments.

   :returns: None


