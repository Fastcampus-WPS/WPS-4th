from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    def to_dict(self):
        ret = {
            'pk': self.pk,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
        return ret
