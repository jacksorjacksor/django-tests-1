from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.QuestionListView.as_view(), name="index"),
    path("<int:pk>/", views.QuestionDetailView.as_view(), name="details"),
    path("<int:pk>/results/", views.ResultsDetailView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # Template views:
    path("about/", TemplateView.as_view(template_name="polls/about.html")),
]
