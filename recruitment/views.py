from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from . forms import *
from . models import *


class AddMark(View):
    form_class = GradeForm
    template_name = 'recruitment/add_mark.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            task = form.cleaned_data['task']

            try:
                Grade.objects.get(candidate=candidate, task=task)
                messages.warning(request, f'Grade for candidate: {candidate} for task: {task} already exists')

            except Grade.DoesNotExist:
                form.save()
                messages.success(request, f'Grade for candidate: {candidate} for task: {task} has been successfuly addded')
                return redirect('recruitment:main')
        return render(request, self.template_name, {'form': form})


class CandidateList(View):
    def get(self, request, *args, **kwargs):
        candidates = sorted(Candidate.objects.all(), key=lambda x: x.grades_avg(), reverse=True)
        data = []
        for candidate in candidates:
            temporary_dict = {}
            temporary_dict["pk"] = candidate.id
            temporary_dict["full_name"] = candidate.get_full_name()
            temporary_dict["avg_grade"] = candidate.grades_avg()
            temporary_dict["grades"] = candidate.grades()
            data.append(temporary_dict)
        return JsonResponse({"data": data}, safe=False)


class CreateCandidate(View):
    form_class = CandidateForm
    template_name = 'recruitment/create_candidate.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Candidate has been successfuly addded')
            return redirect('recruitment:main')
        return render(request, self.template_name, {'form': form})


class CreateRecruiter(View):
    form_class = RecruiterForm
    template_name = 'recruitment/create_recruiter.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Recruiter has been successfuly addded')
            return redirect('recruitment:main')
        return render(request, self.template_name, {'form': form})


class CreateTask(View):
    form_class = TaskForm
    template_name = 'recruitment/create_task.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task has been successfuly addded')
            return redirect('recruitment:main')
        return render(request, self.template_name, {'form': form})
