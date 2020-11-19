from django.contrib import admin
from .models import Transactions, Mails_for_send

from ckeditor_uploader.widgets import CKEditorUploadingWidget



"""class MovieAdminForm(forms.ModelForm):
    comment = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Transactions
        fields = '__all__'"""



@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
	class Meta:
		verbose_name = 'My image'
		verbose_name_plural = 'My images'

	list_display = ("id" ,"email", "phone_number", "name", "Date")
	list_display_links = ("id" ,)
	search_fields = ("email", "phone_number", "name",)
	readonly_fields = ("email", "phone_number", "name", "Date" , "comment")

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False


# Register your models here.
admin.site.register(Mails_for_send)