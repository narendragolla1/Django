from django.shortcuts import render

# Create your views here.
from app.models import student

def studentview(request):
    student_list=student.objects.order_by('name')
    print(student_list)
    my_dict={'student_list':student_list}
    return render(request,'student.html',context=my_dict)
