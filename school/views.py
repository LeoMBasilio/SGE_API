from .serializers import Student_Serializer, Course_Serializer , Enrollment_Serializer, Enrollment_List_Studant_Serializer, Enrollment_List_Course_Serializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Students, Course, Enrollments
from rest_framework import viewsets, generics

class StudentViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Students.objects.all()
    serializer_class = Student_Serializer

    def get_queryset(self):
        queryset = Students.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)  # Busca parcial e case-insensitive
        return queryset
class CourseViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = Course_Serializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Enrollments.objects.all()
    serializer_class = Enrollment_Serializer

class Enrollment_List_Student(generics.ListAPIView):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Enrollments.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = Enrollment_List_Studant_Serializer

class Enrollment_List_Course(generics.ListAPIView):
    authenthication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Enrollments.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = Enrollment_List_Course_Serializer

    