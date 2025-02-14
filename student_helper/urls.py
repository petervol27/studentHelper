from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("questions/", include("questions.urls")),
    path("tests_sessions/", include("tests_sessions.urls")),
]
