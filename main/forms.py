from .models import Transactions
from django.forms import ModelForm , TextInput , IntegerField ,Textarea
from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class Calculator_form(ModelForm):

	captcha = ReCaptchaField()
	
	class Meta :
		model = Transactions
		fields = ['name', 'email',  'phone_number',  'comment', 'captcha']

		widgets = { 
					"email" : TextInput(attrs={
						'class': 'form_input',
						'placeholder': 'Почта',

						}),


					"name" : TextInput(attrs={
						'class': 'form_input',
						'placeholder': 'ФИО',

						}),

					"phone_number" : TextInput(attrs={
						'class': 'form_input',
						'placeholder': 'телефон',

						}),

					"comment" : Textarea(attrs={
						'class': 'form_comment ',
						'placeholder': 'Комментарий',

						}),


					
					}
