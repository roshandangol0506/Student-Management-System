from django.shortcuts import render

from student_management_app.models import Students, Subjects


def student_home(request):
    students=Students.objects.all()
    return render(request,"student_template/student_home_template.html",{"students":students})