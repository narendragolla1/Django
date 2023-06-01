from django.shortcuts import render

# Create your views here.
from app.forms import studentForm

def student_input_view(request):
    sent=False
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            print('Form validation success')
            print('Name',form.cleaned_data['name'])
            print("Mark",form.cleaned_data['mark'])
            sent=True
    form=studentForm()
    return render(request,'index.html',context={'form':form,'sent':sent})
    