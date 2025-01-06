from django.db import models

class Students(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11)
    birthDate = models.DateField()
    phone = models.CharField(max_length = 14)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ) 
    courseCode = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100, blank = False)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.courseCode

class Enrollments(models.Model):
    PERIOD = (
        ('M','Morning'),
        ('A','Afternoon'),
        ('N','Night'),
    )
    student = models.ForeignKey(Students, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    period = models.CharField(max_length = 1, choices = PERIOD, blank = False, null = False, default = 'M')
