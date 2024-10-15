seshat.apps.accounts.custom_validators
======================================

.. py:module:: seshat.apps.accounts.custom_validators


Functions
---------

.. autoapisummary::

   seshat.apps.accounts.custom_validators.validate_email_with_dots


Module Contents
---------------

.. py:function:: validate_email_with_dots(value)

   Custom validator to reject email addresses with more than four dots in
   their domain part.

   :param value: The email address to validate.
   :type value: str

   :returns: None

   :raises ValidationError: If the email address contains more than four dots in
       the domain part.


