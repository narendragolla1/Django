from django.urls import path
from . import views
urlpatterns = [
    path('',views.drf_HTML_Response)
]
