
from .models import question_answer
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import TextInput
from django.db import models



# Register your models here.


class question_answerAdminForm(forms.ModelForm):
    answer = forms.CharField(label="текст", widget=CKEditorUploadingWidget())

    class Meta:
        model = question_answer
        fields = '__all__'


@admin.register(question_answer)
class question_answerAdmin(admin.ModelAdmin):
	form = question_answerAdminForm
	list_display = ("question",)
	formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        
    }