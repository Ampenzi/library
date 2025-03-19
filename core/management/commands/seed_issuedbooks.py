import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from core.models import IssuedBook, Book  # Adjust the import based on your app structure
from django.utils.timezone import now, timedelta

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with dummy issued books"

    def handle(self, *args, **kwargs):
        self.stdout.write("📚 Seeding database with dummy issued books...")

        users = list(User.objects.all())  # Get all users
        books = list(Book.objects.all())  # Get all books

        if not users or not books:
            self.stdout.write(self.style.ERROR("❌ No users or books found! Add some first."))
            return

        for _ in range(30):  # Generate 10 issued books
            student = random.choice(users)  # Pick a random user
            book = random.choice(books)  # Pick a random book
            issuedate = fake.date_between(start_date="-30d", end_date="today")  # Past 30 days
            expirydate = issuedate + timedelta(days=random.randint(7, 30))  # 7-30 days after issue

            IssuedBook.objects.create(
                student=student,
                book=book,
                issuedate=issuedate,
                expirydate=expirydate
            )

        self.stdout.write(self.style.SUCCESS("✅ Dummy issued books added successfully!"))
