from django import forms
from django_app.models import mymodel

class employeeform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = "__all__"