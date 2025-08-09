from django.core.management.base import BaseCommand
from pokeapp.models import CustomUser
from django.db.models import Count

class Command(BaseCommand):
    help = 'List all CustomUser entries with duplicate emails'

    def handle(self, *args, **kwargs):
        duplicates = (
            CustomUser.objects.values('email')
            .annotate(email_count=Count('email'))
            .filter(email_count__gt=1)
        )

        if not duplicates:
            self.stdout.write("No duplicate emails found.")
            return

        self.stdout.write("Duplicate emails found:")
        for dup in duplicates:
            email = dup['email']
            count = dup['email_count']
            self.stdout.write(f"Email: {email} - Count: {count}")
            users = CustomUser.objects.filter(email=email)
            for user in users:
                self.stdout.write(f"  User ID: {user.id}, Name: {user.first_name}, Email: {user.email}")
