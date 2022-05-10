from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'text': '내용'
        }