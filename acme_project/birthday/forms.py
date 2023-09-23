from django import forms

from .models import Birthday

class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widget = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
