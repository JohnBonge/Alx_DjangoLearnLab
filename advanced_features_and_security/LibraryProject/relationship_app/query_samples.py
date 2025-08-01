import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Replace with actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Jane Austen"
author = Author.objects.get(name=author_name)
book = Book.objects.filter(author=author)

for book in books:
	print(book.title)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian at {library_name}: {librarian.name}")
