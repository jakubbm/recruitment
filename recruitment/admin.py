from django.contrib import admin
from . models import *

admin.site.register(Recruiter),
admin.site.register(Candidate),
admin.site.register(Task),
admin.site.register(Grade)