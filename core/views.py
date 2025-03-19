from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib.auth.models import User

from .models import (
    Book,
    IssuedBook,
)

def home_view(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request, 'store/index.html', context=context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically login after registration
            messages.success(request, "✅ Registration successful!")
            return redirect('login')  # Redirect to login page

    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})

def get_expiry():
    """Returns the expiry date 15 days from today"""
    return datetime.today().date() + timedelta(days=15)

@login_required(login_url='login')
def borrow_book(request, book_id):
    """Handles borrowing of books"""
    book = get_object_or_404(Book, id=book_id)

    # Get the logged-in student (assuming user email matches Student email)
    user = User.objects.get(id=request.user.id)
    
    if not user:
        return redirect('home')  # Ensure only students can borrow

    if request.method == "POST":
        IssuedBook.objects.create(
            student=user,
            book=book,
            expirydate=get_expiry(),
        )
        return redirect('home')  # Redirect to home after borrowing

    return redirect('home')


@login_required(login_url='login')
def borrowed_books(request):
    """Show all books borrowed by the logged-in student"""
    
    # Get the logged-in student (assuming the email matches Student email)
    student = User.objects.get(id=request.user.id)

    if not student:
        return render(request, 'store/borrowed.html', {'borrowed_books': None})
    
    # Get all books borrowed by the student
    borrowed_books = IssuedBook.objects.filter(student=student)

    return render(request, 'store/borrowed.html', {'borrowed_books': borrowed_books})