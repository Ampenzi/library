import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with dummy users"

    def handle(self, *args, **kwargs):
        self.stdout.write("👤 Seeding database with dummy users...")

        for _ in range(10):  # Generate 10 users
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}{random.randint(100, 999)}"
            email = fake.unique.email()
            password = "password123"  # Default password for seeded users

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

        self.stdout.write(self.style.SUCCESS("✅ Dummy users added successfully!"))
