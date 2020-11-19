from django.db import models

class Vacancy(models.Model):
	
	class Meta:
		verbose_name = 'Вакансия'
		verbose_name_plural = 'Вакансии'
		
	name = models.CharField("Должность", max_length = 150)
	cost = models.CharField("Зароботная плата", max_length = 150)
	description = models.TextField("Описание Вакансии ")
	isdraft = models.BooleanField("черновик", default = True)




# Create your models here.
