from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.generate_questions, name="add_question"),
    path("list/", views.list_question, name="list_question"),
    path("submit_answer", views.submit_code, name="submit_answer"),
]
