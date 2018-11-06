from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                 CreateView,UpdateView,DeleteView)
from . import models
# from django.http import HttpResponse

# Create your views here.
# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASED VIEWS ARE COOL!')

class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #school_list is returned as context dictionary

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School



template_name_suffix = '_update_form'
