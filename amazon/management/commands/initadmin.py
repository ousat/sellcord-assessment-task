from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    custom command to create default admin
    """

    def handle(self, *args, **options):
        username = "admin"
        email = "admin@admin.com"
        password = "Test1234"

        if not User.objects.filter(username=username).exists():
            print("Creating account for %s (%s)" % (username, email))
            admin = User.objects.create_superuser(email=email, username=username)
            admin.is_active = True
            admin.set_password(password)
            admin.save()
        else:
            print("Admin account has already been initialized.")
