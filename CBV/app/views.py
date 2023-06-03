from django.shortcuts import render,HttpResponse
from django.views.generic import (
    View,
    TemplateView,
    ListView
    )
from app.models import Book

# Create your views here.
#  They 



# Declaration
class CBV(View):
    # get method is override this method to provide response to the get request
    def get(self,request):
        return HttpResponse("this is for get request")
    

# Template based Application by using CBV
class TemplateCBV(TemplateView):
    tempalate_name="home.html"
    
    
    
#  To list out all the recordings from database table(model) we use ListView
# by default the template name will be modelclassname_list.html  (book_list.html)
# by default the contect object to the template file will be : modelclassname_list (book_list)
class BookListView(ListView):
    model=Book
    #  we can also provide our own context object name 
    #  context_object_name="my_context_object_name"
    # we can also provide our own template file name
    #  template_name="my_template_name"
    
    
    
    