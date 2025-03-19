from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db import models

class Book(models.Model):
    """ Book details """
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
    ]

    name = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField(unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='education')

    def __str__(self):
        return f"{self.name} [{self.isbn}]"
    
def get_expiry():
    '''Default book expiry: 15 days from issue date'''
    return timezone.now().date() + timedelta(days=15)


class IssuedBook(models.Model):
    """ Book issue details """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issued_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='issued_copies')
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)

    def __str__(self):
        return f"{self.student.username} - {self.book.name}"