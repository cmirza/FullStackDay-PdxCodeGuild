from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book, Checkouts
import datetime


# function for index page, get all books from the model, store in context dict and pass to render with index template
def index(request):

    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'library/index.html', context)


# function to update the model, gets all 'checked out' books as book update, gets all books from model as all books.
# loops through all books if book is in checked out books, marks it as checked out and breaks inner loop, otherwise
# book is marked as not checked out
def update(request):
    book_update = request.POST.getlist('books')
    all_books = Book.objects.all()

    for book in all_books:
        for title in book_update:
            if str(book) == str(title):
                book.checked_out = True
                book.save()
                break
            book.checked_out = False
            book.save()

    return HttpResponseRedirect(reverse('library:index'))


# function for checkout page, gets list of completed checkouts, open checkouts and books available for checkout,
# stores them in a context dict and renders them with checkout template
def checkout(request):

    completed_checkouts = Checkouts.objects.exclude(check_in=None)
    open_checkouts = Checkouts.objects.filter(check_in=None)
    ready_books = Book.objects.filter(checked_out=False)

    context = {'ready_books': ready_books, 'open_checkouts': open_checkouts, 'completed_checkouts': completed_checkouts}

    return render(request, 'library/checkout.html', context)


# function for checking out a book, gets entered user name and book from template, checks if either are blank and
# responds with blank checkout page. then builds new Checkout object with book id, username and current date for
# checkout then saves object to model. then updates book in the book in Book model to be checked out and saves.
def check_out(request):
    user_name = request.POST.get('user_name')
    book = request.POST.get('book_id')

    if user_name == '' or book == 'blank':
        return HttpResponseRedirect(reverse('library:checkout'))

    new_checkout = Checkouts(book_id=book, user=user_name, check_out=datetime.datetime.today().strftime('%Y-%m-%d'))
    new_checkout.save()

    update_book = Book.objects.get(id=book)
    update_book.checked_out = True
    update_book.save()

    return HttpResponseRedirect(reverse('library:checkout'))


# function for checking in books, gets checked items from list in template, loops over the list, gets checkout by
# book id and no check in, enters todays date as check in and saves. then gets book from book model, marks not
# as checked out and saves
def check_in(request):

    books_out = request.POST.getlist('checked_out')

    for book in books_out:

        open_checkout = Checkouts.objects.get(book_id=book, check_in=None)
        open_checkout.check_in = datetime.datetime.today().strftime('%Y-%m-%d')
        open_checkout.save()

        update_book = Book.objects.get(id=book)
        update_book.checked_out = False
        update_book.save()

    return HttpResponseRedirect(reverse('library:checkout'))
