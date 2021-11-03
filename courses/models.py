from django.db import models
from students.models import Student

class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    students = models.ManyToManyField(Student, through='StudentsCourse')

    def __str__(self):
        return self.name

class StudentsCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)