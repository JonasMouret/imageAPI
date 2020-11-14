
from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.PhotoList.as_view(), name= 'Photo-List'),
]