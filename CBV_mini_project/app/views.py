from django.shortcuts import render
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
    
    

