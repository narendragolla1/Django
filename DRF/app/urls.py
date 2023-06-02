from django.urls import path
from . import views 
urlpatterns=[
    path('drf/', views.BookList.as_view(), name='books'),
]