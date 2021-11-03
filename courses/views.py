from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic.base import View

from courses.models import Course

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'

class StudentsCourse(View):
    http_method_names = ['get']

    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'courses/Students_Course.html', {'students': course.students.all(), 'course_name': course.name})
