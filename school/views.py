from .serializers import Student_Serializer, Course_Serializer , Enrollment_Serializer, Enrollment_List_Studant_Serializer, Enrollment_List_Course_Serializer
from .models import Students, Course, Enrollments
from rest_framework import viewsets, generics

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = Student_Serializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Course_Serializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollments.objects.all()
    serializer_class = Enrollment_Serializer

class Enrollment_List_Student(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollments.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = Enrollment_List_Studant_Serializer

class Enrollment_List_Course(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollments.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = Enrollment_List_Course_Serializer