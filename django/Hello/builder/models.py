from django.db import models

# Create your models here.
from django.db import models

QUESTION_TYPES = [
    ('mcq', 'Multiple Choice'),
    ('true_false', 'True/False'),
    ('fill_blank', 'Fill in the Blank'),
]

class QuizQuestion(models.Model):
    topic = models.CharField(max_length=200)
    question = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    options = models.JSONField(null=True, blank=True)  # For MCQs
    answer = models.CharField(max_length=100)
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.question[:50]}"

