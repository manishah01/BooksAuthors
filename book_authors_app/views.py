from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author
#book 

def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, 'Index.html', context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
    )
    return redirect('/')

def books(request,book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book':book,
    }
    return render(request,'This_Book.html',context)

def delete_book(request, book_id):
    current_book = Book.objects.get(id=book_id)
    current_book.delete()
    return redirect('/')


# authors 
def authors(request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request,'Authors.html',context)

def add_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def author_info(request,author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.all()
    context = {
        'author' : author,
        'books' : books,
    }
    return render(request,'This_Author.html',context)

def add_book_to_author(request,author_id):
    author = Author.objects.get(id=author_id)
    book_id = request.POST['each_book']
    book = Book.objects.get(id=book_id)
    author.books.add(book)
    author.save()
    return redirect(f'/author_info/{author_id}')

def delete_author(request, author_id):
    current_author = Author.objects.get(id=author_id)
    current_author.delete()
    return redirect(authors)







