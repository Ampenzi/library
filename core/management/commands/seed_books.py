import random
from django.core.management.base import BaseCommand
from faker import Faker
from core.models import Book  # Import your Book model

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with dummy books"

    def handle(self, *args, **kwargs):
        self.stdout.write("📚 Seeding database with dummy books...")

        categories = ['education', 'entertainment', 'comics', 'biography', 'history']

        for _ in range(10):  # Change 10 to any number of records you want
            Book.objects.create(
                name=fake.sentence(nb_words=3),  # Generate a book title with 3 words
                isbn=fake.unique.random_int(min=1000000000, max=9999999999),  # Generate unique ISBN
                author=f"{fake.first_name()} {fake.last_name()}",  # Random author name
                category=random.choice(categories),  # Pick a random category
            )

        self.stdout.write(self.style.SUCCESS("✅ Dummy books added successfully!"))
