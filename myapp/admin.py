from django.contrib import admin
from .models import Application, Job, JobCategory

# Register your models here.
admin.site.register(Application)
admin.site.register(Job)
admin.site.register(JobCategory)
