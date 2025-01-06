from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, Enrollment_List_Student, Enrollment_List_Course
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', Enrollment_List_Student.as_view(), name='enrollments_student'),
    path('courses/<int:pk>/enrollments/', Enrollment_List_Course.as_view(), name='enrollments_course'),
]
