from django.contrib import admin
from django import forms
from .models import Vacancy
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class VacancyAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание Вакансии", widget=CKEditorUploadingWidget())

    class Meta:
        model = Vacancy
        fields = '__all__'

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
	form = VacancyAdminForm
	list_display = ("id" ,"name" , "isdraft")
	list_display_links = ("name" ,)
# Register your models here.
