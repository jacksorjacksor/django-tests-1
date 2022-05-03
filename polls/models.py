import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    """Model definition for Question."""

    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField(
        "date published", auto_now=False, auto_now_add=False
    )

    class Meta:
        """Meta definition for Question."""

        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        """Unicode representation of Question."""
        return self.question_text

    # METHODS
    # ADMIN
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        return (
            timezone.now()
            >= self.pub_date
            >= (timezone.now() - datetime.timedelta(days=1))
        )


class Choice(models.Model):
    """Model definition for Choice."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        """Meta definition for Choice."""

        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        """Unicode representation of Choice."""
        return self.choice_text
