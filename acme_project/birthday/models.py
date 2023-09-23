from django.db import models

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения') 




class ContestForm(forms.Form):
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Contest
        # Указываем, что надо отобразить все поля.
        fields = '__all__' 
        
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
        }
        widgets = {
            'comment': forms.Textarea({'cols': '22', 'rows': '5'}),
        }
        
from django.db import models

# Опишите модель Contest здесь!
class Contest(models.Model):
    title = forms.CharField('Название', max_length=20)
    description = forms.TextField('Описание')
    price = forms.IntegerField('Цена',
                MinValueValidator=10,
                MaxValueValidator=100,
                help_text='Рекомендованная розничная цена')
    comment = forms.TextField('Комментарий',
        blank=False)