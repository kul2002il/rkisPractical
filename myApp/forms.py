from django import forms

from .models import User


class ChangeUserInfoForm(forms.ModelForm):
	fio = forms.CharField(required=True, label='Отчество')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'fio')
