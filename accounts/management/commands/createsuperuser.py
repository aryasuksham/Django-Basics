from django.core.management.commands.createsuperuser import Command as BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with a phone number as the identifier'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        username = input('Enter phone number: ')
        password = input('Enter password: ')

        User.objects.create_superuser(
            phone_number=username,
            password=password
        )

        self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
