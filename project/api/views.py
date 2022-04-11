from functools import partial
from os import stat
from urllib.request import Request
from requests import delete, request
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student, Course, Subject, Enrollment
from .serializer import StudentSerializer, SubjectSerializer, CourseSerializer, EnrollmentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics

from api import serializer

class StudentView(APIView):
    def get(self, request, id=None):
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'student created', 'data':serializer.data})
    def put(self, request, id):
        data = request.data
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'student updated', 'data':serializer.data})
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response({'message':'student deleted'})

class SubjectView(APIView):
    def get(self, request, id=None):
        if id is not None:
            subject = Subject.objects.get(id=id)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'subject created', 'data':serializer.data})
    def put(self, request, id):
        data = request.data
        subject = Subject.objects.get(id=id)
        serializer = SubjectSerializer(subject, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'subject updated', 'data':serializer.data})
    def delete(self, request, id):
        subject = get_object_or_404(Subject, id=id)
        subject.delete()
        return Response({'message':'subject deleted'})

class CourseView(APIView):
    def get(self, request, id=None):
        if id is not None:
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'course created', 'data':serializer.data})
    def put(self, request, id):
        data = request.data
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.update(course,data)
            return Response({'message':'course updated', 'data':serializer.data})
    def delete(self, request, id):
        course = get_object_or_404(Course, id=id)
        course.delete()
        return Response({'message':'course deleted'})

class EnrollView(APIView):
    def get(self, request, id=None):
        if id is not None:
            enroll = Enrollment.objects.get(id=id)
            serializer = EnrollmentSerializer(enroll)
            return Response(serializer.data)
        enrolls = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrolls, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'enrollment created', 'data':serializer.data})
    def put(self, request, id):
        data = request.data
        enroll = Enrollment.objects.get(id=id)
        serializer = EnrollmentSerializer(enroll, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'enrollment updated', 'data':serializer.data})
    def delete(self, request, id):
        course = get_object_or_404(Enrollment, id=id)
        course.delete()
        return Response({'message':'enrollment deleted'})
