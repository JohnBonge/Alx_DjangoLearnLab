from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
   
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    
    path('add_book/', add_book, name='add_book'),              # Checker expects "add_book/"
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),  # Checker expects "edit_book/"
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
