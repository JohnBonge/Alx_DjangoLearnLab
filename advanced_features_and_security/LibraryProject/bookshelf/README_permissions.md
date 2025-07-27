# Permissions and Groups Setup

## Custom Permissions (defined in Book model)
- can_view: Can view book list
- can_create: Can add new book
- can_edit: Can update a book
- can_delete: Can remove a book

## Groups Setup (done in Admin)
- Viewers: has `can_view`
- Editors: has `can_view`, `can_create`, `can_edit`
- Admins: has all permissions

## Views with Restrictions
- `/bookshelf/view_books/`: Requires `can_view`
- `/bookshelf/create_book/`: Requires `can_create`
- `/bookshelf/edit_book/<id>/`: Requires `can_edit`
- `/bookshelf/delete_book/<id>/`: Requires `can_delete`
