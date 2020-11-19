from django.urls import path
from .  import views

urlpatterns = [
	path('', views.question_answer.as_view(), name ='question_answer')
]