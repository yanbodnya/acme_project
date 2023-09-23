from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(
        max_length=20, label = 'Имя'
        )
    last_name = forms.CharField(
        label='Фамилия', required=False,
        help_text='Необязательное поле')
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'}))
