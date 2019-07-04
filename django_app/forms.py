from django import forms
from django_app.models import mymodel

class employeeform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = "__all__"

    def clean_eid(self, *args, **kwargs):  # validating existing eid
        inst = self.instance
        eeid = self.cleaned_data.get('eid')
        queryset = mymodel.objects.filter(eid=eeid)
        
        if inst is not None:
            queryset = queryset.exclude(pk = inst.pk)  # excludes the current instance

        if queryset.exists():
            raise forms.ValidationError("bro this employee id is already taken select another one")
        return eeid