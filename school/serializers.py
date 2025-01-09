from rest_framework import serializers
from .models import Students, Course, Enrollments

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'email', 'cpf', 'birthDate', 'phone']

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 digitos!')
        return cpf

class Course_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Enrollment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollments
        exclude = []

class Enrollment_List_Studant_Serializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollments
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
    
class Enrollment_List_Course_Serializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source = 'student.name')
    class Meta:
        model = Enrollments
        fields = ['student']