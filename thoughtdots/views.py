from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from thoughtdots.models import Data_Set

def index(request):
	context = {

	}
	return render(request, 'index.html', context)

class DataSetCreateView(CreateView):
	model = Data_Set
	template_name = 'data_form.html'
	success_url = '/'