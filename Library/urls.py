from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import (
    home_view,
    register,
    borrow_book,
    borrowed_books,
    book_borrowing_analytics
    )

urlpatterns = [
    # Admin Dashboard
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow'),
    path('borrowed/', borrowed_books, name='borrowed'),
    path("analytics/", book_borrowing_analytics, name="analytics"),
    path('', home_view, name='home'),

]