from django.urls import path
from . import views


urlpatterns = [
    # as_view() we will use when are using class based views
    path('',views.CBV.as_view()),
    path('booklist',views.BookListView.as_view())
    
]
