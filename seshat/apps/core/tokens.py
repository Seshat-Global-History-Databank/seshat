from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    A class to generate a token for account activation.
    """

    def _make_hash_value(self, user, timestamp):
        """
        A method to make a hash value for the token. The hash value is based
        on the user's primary key, the timestamp, and the email confirmation
        status.

        Args:
            user (User): The user object.
            timestamp (int): The timestamp.

        Returns:
            str: The hash value.
        """
        return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.profile.email_confirmed))


account_activation_token = AccountActivationTokenGenerator()
