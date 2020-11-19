from django.db import models

from django.utils import timezone

class Novelty(models.Model):
	class Meta:
		verbose_name = 'Новости'
		verbose_name_plural = 'Новость'
	"""docstring for ClassName"""

	title = models.CharField("заголовок", max_length = 150)
	post = models.TextField("текст")
	date = models.DateField("дата",default = timezone.now )
	isdraft = models.BooleanField("черновик", default = True)
	



	def __str__(self):
		return self.title

# Create your models here.
