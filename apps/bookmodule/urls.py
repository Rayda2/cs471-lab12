from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_books/', views.list_books, name='list_books'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('<int:bookId>/', views.viewbook, name='view_one_book'),
    path('html5/links/', views.links, name='html5_links'),
    path('html5/text/formatting/', views.formatting, name='html5_formatting'),
    path('html5/listing/', views.listing, name='html5_listing'),
    path('html5/tables/', views.tables, name='html5_tables'),
    path('search/', views.search, name='books.search'),
    path('simple/query/', views.simple_query),
    path('complex/query/', views.lookup_query),
    path('lab9/task1', views.task1),
    path('lab9/task2', views.task2),
    path('lab9/task3', views.task3),
    path('lab9/task4', views.task4),
    path('lab9/task5', views.task5),
    path('lab9/task6', views.task6),
    path('lab9_part1/listbooks', views.list_books_crud),
    path('lab9_part1/addbook', views.add_book),
    path('lab9_part1/editbook/<int:id>', views.edit_book),
    path('lab9_part1/deletebook/<int:id>', views.delete_book),
    path('lab9_part2/listbooks', views.list_books_form),
    path('lab9_part2/addbook', views.add_book_form),
    path('lab9_part2/editbook/<int:id>', views.edit_book_form),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_form),
    path('lab11/task1/list', views.student11_list),
    path('lab11/task1/add', views.student11_add),
    path('lab11/task1/edit/<int:id>', views.student11_edit),
    path('lab11/task1/delete/<int:id>', views.student11_delete),
    path('lab11/task2/list', views.student22_list),
    path('lab11/task2/add', views.student22_add),
    path('lab11/task2/edit/<int:id>', views.student22_edit),
    path('lab11/task2/delete/<int:id>', views.student22_delete),
    path('lab11/task3/add', views.product11_add),
    path('lab11/task3/list', views.product11_list),
] 