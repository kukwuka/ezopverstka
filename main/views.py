from django.shortcuts import render

from .forms import Calculator_form
from .models import Transactions
from django.views.generic import CreateView



def index(request):
	"""eror = ''
	if request.method == 'POST':
		form = Calculator_form(request.POST)
		if form.is_valid():
			form.save()
		else:
			eror = 'Форма не отправлена'


		"""
	
	return render(request, 'main/main.html' )



def diagnostics(request):
	
	return render(request, 'main/diagnostics.html' )


def design(request):
	
	return render(request, 'main/design.html' )



def development(request):
	
	return render(request, 'main/development.html' )


def Installation_and_repair(request):
	
	return render(request, 'main/Installation_and_repair.html' )


def HVT(request):
	
	return render(request, 'main/HVT.html' )


class ContactView(CreateView):
	model = Transactions
	form_class = Calculator_form
	success_url = "/"



def groza(request):
	
	return render(request, 'main/groza.html' )





 	

	

	












	


# Create your views here.
