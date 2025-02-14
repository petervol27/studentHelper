from django.db import models

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    QUESTION_TYPES = [
        ('mcq', 'MCQ'),
        ('tf', 'TF'),
        ('open', 'Open'),
    ]  

    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    result = models.TextField()  
    type = models.TextField(max_length=20, choices='topicBased') 
    topic = models.TextField()
    language = models.TextField(default="English")  
    questionType = models.CharField(max_length=20, choices=QUESTION_TYPES, default='mcq')  # Changed to CharField for questionType

    def __str__(self):
        return f"{self.difficulty} - {self.description[:50]}"
