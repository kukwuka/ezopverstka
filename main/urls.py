from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('diagnostics', views.diagnostics, name ='diagnostics'),
    path('design', views.design, name ='design'),
    path('development', views.development, name ='development'),
    path('Installation_and_repair', views.Installation_and_repair, name ='Installation_and_repair'),
    path('HVT', views.HVT, name ='HVT'),
    path('contact', views.ContactView.as_view(), name="contact"),
	path('groza', views.groza, name="groza")
]