from django.shortcuts import render
from .models import Novelty
from django.views.generic import ListView , DetailView


def news(request):
	"""eror = ''
	if request.method == 'POST':
		form = Calculator_form(request.POST)
		if form.is_valid():
			form.save()
		else:
			eror = 'Форма не отправлена'



	form = Calculator_form()



	data = {
		'form' :form,
		'eror' :eror
	}
	return render(request, 'main/main.html' , data) 
	"""
	




	return render(request, 'news/news.html' )




class NoveltyView(ListView):
	paginate_by = 14
	model = Novelty
	
	context_object_name = "Novelty" 
	template_name = "news/news.html"


	def get_queryset(self):
		return Novelty.objects.filter(isdraft=False)[::-1]


class NoveltyDetailView(DetailView):
	model = Novelty
	queryset = Novelty.objects.all()
	context_object_name = "post" 
	template_name = "news/deatails_view.html"
	


# Create your views here.
