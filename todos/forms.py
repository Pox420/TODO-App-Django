from django import forms
from .models import MyTodo


class TodoForm(forms.ModelForm):
    class Meta:
        model = MyTodo
        fields = ('title', 'completed')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your todo here'
            })
        }
