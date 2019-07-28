from django import forms
from django_app.models import mymodel, student, transaction, librarian

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

class loginform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['enrollment', 'password']
        widgets = {
            'enrollment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enrollment No.'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

class libloginform(forms.ModelForm):
    class Meta:
        model = librarian
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

class fee_request_form(forms.ModelForm):
    # receipt_date = forms.DateField(
    #     widget=forms.DateInput(format=('%d-%m-%Y'), 
    #                            attrs={'class':'form-control', 
    #                            'placeholder':'Select a date'}))
    class Meta:
        model = transaction
        fields = [
            'status',
            'receipt_no',
            'receipt_date',
            'amount',
            'student_enrollment',
            'fee_receipt_image',
            'cancelled_cheque_image',
            'passbook_image',
            'last_sem_fee_image',
            'grade_history_image',
        ]
        widgets = {
            # 'application_no' : forms.TextInput(attrs= {'class': 'form-control', 'readonly':'readonly'})
            'receipt_no' : forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Receipt No."}),
            'receipt_date' : forms.DateInput(attrs = {"class":"form-control", "placeholder": "mm/dd/yyyy"}, format=("%m/%d/%Y") ),
            'amount' : forms.NumberInput(attrs = {"class":"form-control", "placeholder":"Library Fee Amount"}),
            'student_enrollment' : forms.TextInput(attrs = {"class":"form-control", "readonly":"", 'placeholder':"e.g: 175170693016"}),
            'fee_receipt_image' : forms.FileInput(attrs = {"class":"form-control"}),
            'passbook_image' : forms.FileInput(attrs = {"class":"form-control"}),
            'cancelled_cheque_image' : forms.FileInput(attrs = {"class":"form-control"}),
            'last_sem_fee_image' : forms.FileInput(attrs = {"class":"form-control"}),
            'grade_history_image' : forms.FileInput(attrs = {"class":"form-control"}),
        }