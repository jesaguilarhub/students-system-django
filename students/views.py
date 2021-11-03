from django.views.generic import ListView, DetailView

from students.models import Student

class StudentsListView(ListView):
    model = Student
    context_object_name = 'students'

class StudentDetailView(DetailView):
    queryset = Student.objects.all()
    context_object_name = 'student'