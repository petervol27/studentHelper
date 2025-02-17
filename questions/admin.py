from django.contrib import admin
from .models import Question

# Register your Question model with the Django admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'difficulty', 'result')
    search_fields = ('description', 'difficulty')
    list_filter = ('difficulty',)

admin.site.register(Question, QuestionAdmin)
