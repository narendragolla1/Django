from django.shortcuts import render,HttpResponse
from app.models import Company
from django.urls import reverse_lazy
from django.views.generic import (
CreateView,
ListView,   
DetailView,
UpdateView,   
DeleteView                           
                                  
)
# Create your views here.

class CompanyListView(ListView):
    model=Company
    template_name='company_list.html'

class CompanyDetailView(DetailView):
    model=Company
    template_name='company_detail.html'
    
class CompanyCreateView(CreateView):
    model=Company
    field=('name','location','ceo')
    
class CompanyUpdateView(UpdateView):
    model=Company
    field=('name','ceo')
    
class CompanyDeleteView(DeleteView):
    model=Company
    template_name='company_delete.html'
    success_url=reverse_lazy('companies')
    


def index(request,id):
    data = [
        {'id': 10, 'name': 'chaitanya', 'location': 'epuru'},
        {'id': 11, 'name': 'narayana', 'location': 'eluru'},
        {'id': 12, 'name': 'narayana', 'location': 'eluru'}
    ]

    context = {'data': data}
    return render(request, 'details.html', context)
    
    

