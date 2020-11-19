from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .mail_service import send_mail_global
from django.template import loader
import datetime

class Transactions(models.Model):

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'

	name = models.CharField("ФИО", max_length=150 )
	email = models.CharField("почта", max_length=150, default="")
	phone_number = models.CharField("номер телефона", max_length=12 )
	Date =  models.DateTimeField("дата", auto_now_add = True)
	comment = models.TextField("Комметнарий",blank=True)
	note = models.TextField("Примечание",blank=True)
	

	def __str__(self):
		return self.name


class Mails_for_send(models.Model):
	class Meta:
		verbose_name = 'Адресант'
		verbose_name_plural = 'Адресанты'

	mail_url = models.CharField("почта", max_length=150 )


	def __str__(self):
		return self.mail_url







@receiver(pre_save, sender=Transactions)
def send_save_mail(sender, instance, **kwargs):
	print("sending")

	mails_result = []
	print(Mails_for_send.objects.all())

	subject = "обратная связь от " + instance.name + " почта: " + instance.email
	

	html_message = loader.render_to_string(
            'main/mail_template.html',
			{
                'user_name': instance.name,
                'user_mail':  instance.email,
                'user_phone' : instance.phone_number,
                'user_comment': instance.comment,

            }
        )

	for i in Mails_for_send.objects.all():
		print(i.mail_url)
		mails_result.append(i.mail_url)

	send_text = "обратная связь от " + instance.name + "/n" + "почта:"  + instance.email + "/n" + "телефон:" + instance.phone_number + "/n" + "Текст : /n" + instance.comment

	
	print(mails_result)
	send_mail_global( subject , send_text , 'ezop.site@mail.ru' , mails_result ,html_message)	
	print("sended")





# Create your models here.
