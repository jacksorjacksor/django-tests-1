from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django import forms

from .models import Question, Choice


class QuestionListView(ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()


class QuestionDetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsDetailView(DetailView):
    model = Question
    template_name = "polls/results.html"


# LOGIC
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "NOOOOOO"},
        )
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
