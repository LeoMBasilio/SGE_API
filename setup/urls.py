from school.views import StudentViewSet, CourseViewSet
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
