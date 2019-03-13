from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models

class IndexView(TemplateView):
    template_name = 'first_app/index.html'
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'first_app/school_detail.html'

