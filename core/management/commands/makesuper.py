from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
import environ

env = environ.Env()


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            try:
                User.objects.create_superuser(env("ADMINNAME"),
                                              env("ADMINMAIL"),
                                              env("ADMINPASSWORD"))
                self.stdout.write(self.style.SUCCESS('Admin user has created'))
            except ImproperlyConfigured:
                self.stdout.write(
                    self.style.ERROR('Admin environment name not found'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))
