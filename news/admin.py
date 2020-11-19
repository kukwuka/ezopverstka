from django.contrib import admin
from django import forms

from .models import Novelty
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import TextInput
from django.db import models



class NoveltyAdminForm(forms.ModelForm):
    post = forms.CharField(label="текст", widget=CKEditorUploadingWidget())

    class Meta:
        model = Novelty
        fields = '__all__'


# Register your models here.

@admin.register(Novelty)
class NoveltysAdmin(admin.ModelAdmin):
	form = NoveltyAdminForm
	list_display = ("id" ,"title", "date", "isdraft") 
	list_display_links = ("id" ,"title")
	search_fields = ("title" ,)
	formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        
    }
