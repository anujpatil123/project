from django.contrib import admin

# Register your models here.
from .models import QuizQuestion

admin.site.register(QuizQuestion)
