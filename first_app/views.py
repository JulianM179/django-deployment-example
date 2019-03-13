from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy

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
class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("first_app:list")