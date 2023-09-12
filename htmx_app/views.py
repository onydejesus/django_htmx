from django.shortcuts import render
from .forms import BookForm
from .models import Book


def index_view(request):
    books = Book.objects.all()
    context = {
            "books": books,
            "form": BookForm(),
    }
    return render(request, 'htmx_app/index.html', context)


def create_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            context = {
                'book': book
            }
            return render(request, 'htmx_app/partials/book_list.html', context)
    return render(request, 'htmx_app/partials/book_create.html', {'form': BookForm()})
