from django.shortcuts import render
from .models import Student
# Create your views here.

def get_student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'app/index.html', context)