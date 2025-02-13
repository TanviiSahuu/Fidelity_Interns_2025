from django import forms
from stocks_app.models import stocks

class stockforms(forms.ModelForm):
    class Meta:
        model = stocks
        fields = '__all__'