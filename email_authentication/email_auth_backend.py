from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from swingtime.models import Event


class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.
    """

    def authenticate(self, email=None, name=None, password=1):
        if email and name:
            try:
                user = User.objects.get(email=email, username=name)
                return user
            except User.DoesNotExist:
                try:
                    if Event.objects.get(email=email, name=name):
                        user = User.objects.create_user(email=email, username=name, password=password)
                        return user
                except Event.DoesNotExist:
                    return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
