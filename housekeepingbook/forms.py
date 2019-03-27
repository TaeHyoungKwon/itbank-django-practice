from django import forms

from .models import HouseKeepingBook


class HouseKeepingBookForm(forms.ModelForm):
    class Meta:
        model = HouseKeepingBook
        fields = '__all__'
