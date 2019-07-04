from django import forms
from django_app.models import mymodel

class employeeform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = "__all__"

    def clean_eid(self, *args, **kwargs):
        eeid = self.cleaned_data.get('eid')
        queryset = mymodel.objects.filter(eid=eeid)
        if queryset.exists():
            print("locha hai")
            raise forms.ValidationError("bro this employee id is already taken select another one")
        return eeid