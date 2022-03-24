from django.forms import ModelForm
from .models import BackForm


class BackForms(ModelForm):
    class Meta:
        model = BackForm
        fields = ['name', 'phone', 'email']
