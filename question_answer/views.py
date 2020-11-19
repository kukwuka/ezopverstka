from django.shortcuts import render
from .models import question_answer as question_answer_model
from django.views.generic import ListView , DetailView





class question_answer(ListView):
	paginate_by = 5
	model = question_answer_model
	
	context_object_name = "questions_answers" 
	template_name = 'question_answer/question_answer.html'


	def get_queryset(self):
		return question_answer_model.objects.filter(isdraft=False)[::-1]