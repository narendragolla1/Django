from django.urls import path
from . import views
urlpatterns = [
    path('',views.CompanyListView.as_view()),
    path('app/<int:id>',views.index),
]
