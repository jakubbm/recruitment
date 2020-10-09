from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def grades(self):
        grades = self.grade_set.all()
        grades_list = [grade.value for grade in grades]
        return grades_list

    def grades_avg(self):
        grades_list = self.grades()
        lenght = len(grades_list)
        if lenght == 0:
            avg = 0
        else:
            avg = round(sum(grades_list)/lenght, 2)
        return avg


class Recruiter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Grade(models.Model):
    value = models.PositiveSmallIntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, null=True, on_delete=models.SET_NULL)