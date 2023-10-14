from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # Use the user's primary email address as part of the token hash
        # (You can customize this based on your application's requirements)
        return (
            str(user.pk) + user.email + str(timestamp) +
            str(user.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()
