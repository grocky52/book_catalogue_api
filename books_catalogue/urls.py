from django.urls import path
from books_catalogue.views import BookList, CreateBooks, book

app_name = 'books_catalogue'
urlpatterns = [
    path('', BookList.as_view(), name='booklist'),
    path('create/', CreateBooks.as_view(), name='create_books'),
    path('book/<int:pk>/', book.as_view(), name='crud_book'),
    
]