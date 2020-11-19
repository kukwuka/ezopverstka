from django.core.mail import send_mail


def send_mail_global(subject , message , host_mail ,  user_email, html_message):
	print("function")
	print( host_mail)
	try:
		send_mail(
		subject,
		message, 
		host_mail,
		user_email,
		fail_silently= True,
		html_message = html_message
	)
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass
	
	