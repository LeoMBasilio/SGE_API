from django.contrib import admin
from .models import Students, Course, Enrollments

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'birthDate', 'phone')
    list_display_links = ('name', 'email')
    list_per_page = 10
    search_fields = ('name', 'email', 'cpf')

admin.site.register(Students, StudentsAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'description', 'level')
    list_display_links = ('courseCode', 'description')
    list_per_page = 10
    search_fields = ('courseCode', 'description')

admin.site.register(Course, CourseAdmin)

class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'period')
    list_display_links = ('student', 'course')
    list_per_page = 10
    search_fields = ('student', 'course')

admin.site.register(Enrollments, EnrollmentsAdmin)