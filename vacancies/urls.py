from django.urls import path
from .  import views


urlpatterns = [

    path('', views.VacanciesView.as_view(), name ='vacancies'),
    path('<int:pk>' , views.VacancyDetailView.as_view() , name = 'vacancies_detail' )
    
]