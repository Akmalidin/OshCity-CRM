from django import forms
from .models import Expend

class ExpendForm(forms.ModelForm):
    expend_type = forms.CharField(widget=forms.HiddenInput(), required=False)  # Убираем обязательность

    class Meta:
        model = Expend
        fields = ['expend_type', 'description', 'user', 'start_date', 'end_date', 'amount', 'status', 'is_salary_confirmed']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Пользователь'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'С даты'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'По дату'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Сумма'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_salary_confirmed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        expend_type = cleaned_data.get('expend_type')
        description = cleaned_data.get('description')
        user = cleaned_data.get('user')

        # Проверка: если выбран тип "Другое", поле description должно быть заполнено
        if expend_type == 'other' and not description:
            self.add_error('description', 'Описание обязательно для типа "Другое".')
        elif expend_type == 'salaries' and not user:
            self.add_error('user', 'Пользователь обязателен для типа "Зарплаты".')
