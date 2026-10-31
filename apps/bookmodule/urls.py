from django.urls import path
from . import views

urlpatterns = [
    path('<int:bookId>', views.viewbook),
]

# Lab 5 - Task 1
urlpatterns += [
    path('html5/links/', views.links_view, name='books.html5_links'),
]

# Lab 5 - Task 2
urlpatterns += [
    path('html5/text/formatting/', views.text_formatting_view,
         name='books.html5_formatting'),
]

# Lab 5 - Task 3
urlpatterns += [
    path('html5/listing/', views.listing_view, name='books.html5_listing'),
]

# Lab 5 - Task 4
urlpatterns += [
    path('html5/tables/', views.tables_view, name='books.html5_tables'),
]
