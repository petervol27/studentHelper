from django.contrib import admin
from .models import StudentUser

# Register your custom user model with the Django admin
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'age', 'city', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(StudentUser, StudentUserAdmin)
