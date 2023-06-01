from django.shortcuts import render
from . import forms
from app.models import student
# Create your views here.

def student_view(request):
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'index.html',{'form':form})
        