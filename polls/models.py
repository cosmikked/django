import datetime

from django.db import models
from django.utils import timezone 

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published") # first argument is custom column name 

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # foreign key automatically referring to pk of Questions
    # can be changed in to_field attribute
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(db_default=0)

    def __str__(self):
        return self.choice_text
