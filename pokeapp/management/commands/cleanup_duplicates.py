from django.core.management.base import BaseCommand
from pokeapp.models import CustomUser
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate CustomUser entries with the same email, keeping the earliest created'

    def handle(self, *args, **kwargs):
        duplicates = (
            CustomUser.objects.values('email')
            .annotate(email_count=Count('email'))
            .filter(email_count__gt=1)
        )

        total_removed = 0
        for dup in duplicates:
            email = dup['email']
            users = CustomUser.objects.filter(email=email).order_by('id')
            # Keep the first user, delete the rest
            to_delete = users[1:]
            count = to_delete.count()
            to_delete.delete()
            self.stdout.write(f"Removed {count} duplicate users with email: {email}")
            total_removed += count

        self.stdout.write(self.style.SUCCESS(f"Total duplicate users removed: {total_removed}"))
