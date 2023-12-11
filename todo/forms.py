# forms.py
from django import forms
from .models import Todo,DeletedTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task','description']

class DeleteForm(forms.ModelForm):
    class Meta:
        model = DeletedTask
        fields = ['task','description']
