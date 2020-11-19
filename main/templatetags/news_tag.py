from django import template
from news.models import Novelty
from main.forms import Calculator_form


register = template.Library()


@register.simple_tag()
def get_Novelty():
	if len(Novelty.objects.filter(isdraft=False)) < 6:
		return Novelty.objects.filter(isdraft=False)[::-1]
	else :
		return Novelty.objects.filter(isdraft=False)[len(Novelty.objects.filter(isdraft=False))-6:len(Novelty.objects.filter(isdraft=False)):-1]


@register.simple_tag()
def get_FormDirection():
	form = Calculator_form()
	
	return form 
