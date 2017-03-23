from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from config.settings import config

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        superuser_username = config['django']['superuser']['username']
        superuser_password = config['django']['superuser']['password']
        superuser_email = config['django']['superuser']['email']

        if not User.objects.filter(username=superuser_username).exists():
            User.objects.create_superuser(
                username=superuser_username,
                password=superuser_password,
                email=superuser_email
            )
