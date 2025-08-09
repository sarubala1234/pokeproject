from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    """
    Custom authentication backend to authenticate users using their email address.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')
        try:
            # Use filter and first() to avoid MultipleObjectsReturned
            user = UserModel.objects.filter(email__iexact=username).first()
        except UserModel.DoesNotExist:
            return None
        else:
            if user and user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
