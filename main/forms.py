from django import forms
from .models import Item



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item # Сощдаем форму на базе модели Item
        fields = ['theme', 'text']  
        labels = {'theme': '', 'text': ''} 
