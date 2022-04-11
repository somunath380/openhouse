from rest_framework import serializers
from .models import Student, Course, Subject, Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
        depth = 1

class StudentSerializer(serializers.ModelSerializer):
    student_enrolled = EnrollmentSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_enrolled']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')

class CourseSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Course
        fields = ['id', 'name', 'subjects']
        depth=1
      
