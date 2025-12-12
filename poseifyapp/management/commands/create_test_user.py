from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a test user'

    def handle(self, *args, **options):
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user('testuser', 'test@example.com', 'testpassword')
            self.stdout.write(self.style.SUCCESS('Successfully created test user'))
        else:
            self.stdout.write(self.style.WARNING('Test user already exists'))
