from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import CustomerProfile

class Command(BaseCommand):
    help = 'Ensures all users have associated profiles'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        created_count = 0
        
        for user in users_without_profiles:
            CustomerProfile.objects.create(user=user)
            created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} missing user profiles'
            )
        )
