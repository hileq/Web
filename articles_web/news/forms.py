from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesFrom(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nagłówek artykułu'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Zapowiedź'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Cały tekst'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data i czas'
            })
        }