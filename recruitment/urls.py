from django.urls import path
from . import views


app_name = "recruitment"

urlpatterns = [
    path('add-mark', views.AddMark.as_view(), name="main"),
    path('create_candidate', views.CreateCandidate.as_view(), name="candidate"),
    path('create_recruiter', views.CreateRecruiter.as_view(), name="recruiter"),
    path('create_task', views.CreateTask.as_view(), name="task"),
    path('candidateList', views.CandidateList.as_view(), name="list"),
]
