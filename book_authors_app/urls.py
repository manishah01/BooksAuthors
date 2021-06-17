from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book',views.add_book),
    path('books/<int:book_id>',views.books),
    path('author_info/<int:author_id>/add',views.add_book_to_author),
    path('delete_book/<int:book_id>',views.delete_book),
    path('add_author',views.add_author),
    path('authors',views.authors),
    path('author_info/<int:author_id>',views.author_info),
    path('delete_author/<int:author_id>',views.delete_author),
]