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
		nation = Country.objects.all()[0]

		context['startyear'] = nation.data.all()[0].year
		context['endyear'] = nation.data.all().reverse()[0].year

		return context

class DataSetCreateView(CreateView):
	model = Data_Set
	template_name = 'data_form.html'
	success_url = '/1/'

def about(request):
	return render(request, 'about.html')

def guide(request):
	return render(request, 'guide.html')