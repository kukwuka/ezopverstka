from django.db import models

class question_answer(models.Model):
	class Meta:
		verbose_name = 'Вопрос-ответ'
		verbose_name_plural = 'Вопрос-ответ'
	"""docstring for ClassName"""

	question = models.CharField("вопрос", max_length=300 )
	answer = models.TextField("ответ")
	isdraft = models.BooleanField("черновик" , default = True)
	



	def __str__(self):
		return self.question


# Create your models here.
