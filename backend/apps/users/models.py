from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Default user
    """

    def __str__(self):
        return self.username
