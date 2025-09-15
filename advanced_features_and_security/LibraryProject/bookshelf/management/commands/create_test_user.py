from django.core.management.base import BaseCommand
from bookshelf.models import CustomUser

class Command(BaseCommand):
    help = 'Create a test user for testing'

    def handle(self, *args, **options):
        user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpassword123',
            first_name='Test',
            last_name='User',
            date_of_birth='1990-01-01'
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully created test user: {user.email}'))
