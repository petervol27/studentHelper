from django.db import models
from students.models import StudentUser
from questions.models import Question
from datetime import timedelta, datetime

class TestSession(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateField()
    given_answer = models.TextField()
    success = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Check if the given answer matches the result and set success accordingly
        self.success = self.given_answer.strip() == self.question.result.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.username} - {self.question.difficulty}"
