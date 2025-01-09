from rest_framework import serializers
from .models import Students, Course, Enrollments
from .validators import invalidCpf, invalidName, invalidPhone

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'email', 'cpf', 'birthDate', 'phone']

    def validate(self, data):
        if invalidCpf(data['cpf']):
            raise serializers.ValidationError({'cpf:':' O CPF nao e valido!'})
        if invalidName(data['name']):
            raise serializers.ValidationError({'name':' O nome deve conter somente leras'})
        if invalidPhone(data['phone']):
            raise serializers.ValidationError({'phone':' O celular deve conter 13 digitos'})
        return data

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