from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, label=_('Parol takror'))

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError(_('Parollar bir xil emas !'))

        return self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': _('Login'),
            'password': _('Parol')
        }
        help_texts = {
            'username': _("Lotin hariflaridan iborat bo'lsin.")
        }
        widgets = {
            'password': forms.PasswordInput
        }