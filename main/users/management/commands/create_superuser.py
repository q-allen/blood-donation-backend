from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Create a superuser with credentials from environment variables'

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.getenv('SUPERUSER_EMAIL')
        password = os.getenv('SUPERUSER_PASSWORD')
        username = os.getenv('SUPERUSER_USERNAME', 'admin')
        first_name = os.getenv('SUPERUSER_FIRST_NAME', 'Admin')
        last_name = os.getenv('SUPERUSER_LAST_NAME', 'User')
        contact = os.getenv('SUPERUSER_CONTACT', '+1234567890')
        address = os.getenv('SUPERUSER_ADDRESS', '123 Admin Street')
        gender = os.getenv('SUPERUSER_GENDER', 'Male')

        if not email or not password:
            self.stdout.write(self.style.ERROR('SUPERUSER_EMAIL and SUPERUSER_PASSWORD must be set in environment variables'))
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Superuser with email {email} already exists'))
            return

        try:
            User.objects.create_superuser(
                email=email,
                password=password,
                username=username,
                first_name=first_name,
                last_name=last_name,
                contact=contact,
                address=address,
                gender=gender,
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser {email} created successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {str(e)}'))