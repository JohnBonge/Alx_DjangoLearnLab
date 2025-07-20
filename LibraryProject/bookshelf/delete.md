from bookshelf.models import Book

book = Book.objects.get(title="Nineteed Eighty-Four")
book.delete()

Book.objects.all()
# <QuerySet []>
