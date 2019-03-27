from .models import NameCard
from django import forms


class NameCardForm(forms.ModelForm):
    class Meta:
        model = NameCard
        fields = '__all__'
