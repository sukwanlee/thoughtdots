from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from thoughtdots.models import Data_Set, Country, Data_Point

class DataDetailView(DetailView):
	model = Data_Set
	template_name = 'data_detail.html'

	def get_context_data(self, **kwargs):
		context = super(DataDetailView, self).get_context_data(**kwargs)
		context['countries'] = Country.objects.all()
		

		return context

class DataSetCreateView(CreateView):
	model = Data_Set
	template_name = 'data_form.html'
	success_url = '/1/'