from django.urls import path
from .import views


urlpatterns = [
    path('', views.index_view, name='book_list'),
    path("book_create/", views.create_book_view, name="book_create"),
]
