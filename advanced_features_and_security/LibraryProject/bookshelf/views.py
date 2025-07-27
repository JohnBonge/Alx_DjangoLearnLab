from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Book
from django.http import HttpResponse
from django.db.models import Q
from .forms import ExampleForm

form = BookSearchForm(request.GET)
if form.is_valid():
    q = form.cleaned_data['q']
    results = Book.objects.filter(title__icontains=q)

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("Only users with 'can_create' permission can see this.")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse("Only users with 'can_edit' permission can see this.")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse("Only users with 'can_delete' permission can see this.")
# Create your views here.

def search_books(request):
    query = request.GET.get("q", "")
    results = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
    return render(request, "bookshelf/book_list.html", {"books": results, "query": query})

def secure_view(request):
    response = HttpResponse("Secure page")
    response['Content-Security-Policy'] = "default-src 'self';"
    return response

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., save, log, email, etc.)
            return redirect('example_form')  # redirect back to the same form or a success page
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
