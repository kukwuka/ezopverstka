from django.shortcuts import render

from .models import Vacancy
from django.views.generic import ListView , DetailView

def vacancies(request):
	return render(request, 'vacancies/vacancies.html')





class VacanciesView(ListView):
	model = Vacancy
	queryset = Vacancy.objects.filter(isdraft=False)[::-1]
	context_object_name = "Vacancies" 
	template_name = "vacancies/vacancies.html"	
	paginate_by = 6


class VacancyDetailView(DetailView):
	model = Vacancy
	queryset = Vacancy.objects.all()
	context_object_name = "vacancy" 
	template_name = "vacancies/vacancies_detail.html"


# Create your views here.
