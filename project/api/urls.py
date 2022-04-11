
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentView.as_view(), name='students'),
    path('student/<uuid:id>/', views.StudentView.as_view(), name='student'),
    path('subjects/', views.SubjectView.as_view(), name='subjects'),
    path('subject/<uuid:id>/', views.SubjectView.as_view(), name='subject'),
    path('courses/', views.CourseView.as_view(), name='courses'),
    path('course/<uuid:id>/', views.CourseView.as_view(), name='course'),
    path('enrollments/', views.EnrollView.as_view(), name='enrolls'),
    path('enrollment/<uuid:id>/', views.EnrollView.as_view(), name='enroll'),
    
]
