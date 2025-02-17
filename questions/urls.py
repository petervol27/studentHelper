from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_question, name='add_question'),
    path('list/', views.list_question, name='list_question'),
]
