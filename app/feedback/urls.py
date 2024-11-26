from django.urls import path

from . import views

urlpatterns = [
    path("feedback/process/", views.FeedbackView.as_view(), name="bulk-feedback"),
    path("feedback/results/", views.get_task_result, name='results-feedback')
]