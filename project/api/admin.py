from django.contrib import admin
from .models import Student, Subject, Course, Enrollment
# Register your models here.
admin.site.register([Student, Subject, Course, Enrollment])