from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(
            username='lhy',
            email='a@a.com',
            password='dlgksdud',
        )
