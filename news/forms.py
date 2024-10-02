from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add statives'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons statives'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text statives'

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data publicotion'
            }),

        }
