from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book


# function for index page, get all books from the model, store in context dict and pass to render with index template
def index(request):

    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'library/index.html', context)


# function to update the model, gets all 'checked out' books as book update, gets all books from model as all books.
# loops through all books and marks them as not checked out. then loops through all books again, if book is in checked
# out books, marks it as checked out.
def update(request):
    book_update = request.POST.getlist('books')
    all_books = Book.objects.all()

    for book in all_books:
        book.checked_out = False
        book.save()

    for book in all_books:
        for title in book_update:
            if str(book) == str(title):
                book.checked_out = True
                book.save()

    return HttpResponseRedirect(reverse('library:index'))
