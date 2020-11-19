from django.urls import path
from .  import views

urlpatterns = [

    path('', views.NoveltyView.as_view(), name ='news'),
    path('<int:pk>' , views.NoveltyDetailView.as_view() , name = 'news_detail' )
    
]