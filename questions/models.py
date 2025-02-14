from django.db import models

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('intermidiate', 'Intermidiate'),
        ('professional', 'Professional'),
    ]

    # Explicitly defining an id field (this is optional, Django provides it by default)
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES)
    result = models.TextField()

    def __str__(self):
        return f"{self.difficulty} - {self.description[:50]}"
