from ast import Sub
import uuid
from django.db import models
import uuid
# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Subject(models.Model): # publications
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Course(models.Model): # articles
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default=None)
    subjects = models.ManyToManyField(Subject, related_name='course_list')
    
    def __str__(self) -> str:
        return self.name

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_enrolled')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_enrolled')