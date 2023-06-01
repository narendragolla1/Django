from django.shortcuts import render
from app.forms import FeedBackForm
# Create your views here.
def feed_back_form(request):
    form=FeedBackForm()
    if request.method=='POST':
        form=FeedBackForm(request.POST)
        if form.is_valid():
            print('sucessfull')
    return render(request,'index.html',{'form':form})
