from django import forms
from . models import *


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

