import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# This model represents a Question in our poll.
class Question(models.Model):
    # The text of the question. Max length is 200 characters.
    question_text = models.CharField(max_length=200)
    # The date the question was published.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """String representation of the Question object."""
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """
        Custom method to check if the question was published within the last day.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# This model represents a Choice for a specific Question.
class Choice(models.Model):
    # Each choice is related to a single Question.
    # The 'on_delete=models.CASCADE' means that if a Question is deleted,
    # all of its associated Choices will be deleted as well.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # The text of the choice. Max length is 200 characters.
    choice_text = models.CharField(max_length=200)
    # The vote count for this choice, defaults to 0.
    votes = models.IntegerField(default=0)

    def __str__(self):
        """String representation of the Choice object."""
        return self.choice_text
