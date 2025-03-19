from django import forms
from django.contrib.auth.models import User
from .models import Student, Book, IssuedBook

class ContactUsForm(forms.Form):
    """ Contact Form """
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30, 'placeholder': 'Your Message'})
    )


class AdminSignupForm(forms.ModelForm):
    """ Admin Signup Form """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class StudentUserForm(forms.ModelForm):
    """ Student Signup Form """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class StudentForm(forms.ModelForm):
    """ Extra Student Information Form """
    class Meta:
        model = Student
        fields = ['enrollment', 'branch']


class BookForm(forms.ModelForm):
    """ Book Form """
    class Meta:
        model = Book
        fields = ['name', 'isbn', 'author', 'category']


class IssuedBookForm(forms.ModelForm):
    """ Issue Book Form (Now using ForeignKey) """
    class Meta:
        model = IssuedBook
        fields = ['student', 'book']
