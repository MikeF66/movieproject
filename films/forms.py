from .models import Film
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, ClearableFileInput

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'content', 'review', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Введите название фильма'}),
            'description': TextInput(attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Введите описание фильма'}),
            'content': Textarea(attrs={'class': 'form-control', 'id': 'content', 'rows': '5', 'placeholder': 'Введите содержание фильма'}),
            'review': TextInput(attrs={'class': 'form-control', 'id': 'review', 'placeholder': 'Введите отзыв'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Введите дату публикации'})
        }