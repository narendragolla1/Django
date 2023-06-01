from django import forms
from app.models import student

class StudentForm(forms.ModelForm):
    name=forms.CharField()
    roll_no=forms.IntegerField()
    marks=forms.IntegerField()
    class Meta:
        model=student
        fields='__all__'
        
       
    