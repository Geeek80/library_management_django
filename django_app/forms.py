import re, datetime
from django import forms
from django_app.models import mymodel, student, request_transaction, librarian, accountant

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


class loginform(forms.Form):
    enrollment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enrollment No.',
                'autofocus':''
            }
        ),
        max_length=student._meta.get_field('enrollment').max_length
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        max_length=student._meta.get_field('password').max_length
        )

    def clean_enrollment(self, *args, **kwargs):
        data = self.cleaned_data['enrollment']
        if not re.match(r'^\d+$', data):
            raise forms.ValidationError("enrollment can only be of numbers...")
        return data


class libloginform(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'autofocus':''
            }
        ),
        max_length=librarian._meta.get_field('username').max_length
        )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        max_length=librarian._meta.get_field('password').max_length
        )

class acc_login_form(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'autofocus':''
            }
        ),
        max_length=accountant._meta.get_field('username').max_length
        )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        max_length=accountant._meta.get_field('password').max_length
        )

class fee_request_form(forms.ModelForm):
    class Meta:
        model = request_transaction
        fields = [
            'additional_information',
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
            'additional_information' : forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder':'e.g. addmission cancelled'
                    }
                ),
            'receipt_no' : forms.NumberInput(
                attrs = {
                    "class":"form-control",
                    "placeholder":"Receipt No.",
                    'autofocus':''
                    }
                ),
            'receipt_date' : forms.DateInput(
                attrs = {
                    "class":"form-control",
                    "placeholder": "mm/dd/yyyy"
                    },
                format=("%m/%d/%Y")
                ),
            'amount' : forms.NumberInput(
                attrs = {
                    "class":"form-control",
                    "placeholder":"Library Fee Amount"
                    }
                ),
            'student_enrollment' : forms.TextInput(
                attrs = {
                    "class":"form-control",
                    "readonly":"",
                    'placeholder':"e.g: 175170693016"
                    }
                ),
            'fee_receipt_image' : forms.FileInput(
                attrs = {
                    "class":"form-control"
                    }
                ),
            'passbook_image' : forms.FileInput(
                attrs = {
                    "class":"form-control"
                    }
                ),
            'cancelled_cheque_image' : forms.FileInput(
                attrs = {
                    "class":"form-control"
                    }
                ),
            'last_sem_fee_image' : forms.FileInput(
                attrs = {
                    "class":"form-control"
                    }
                ),
            'grade_history_image' : forms.FileInput(
                attrs = {
                    "class":"form-control"
                    }
                ),
        }
    
    def clean_amount(self, *arg, **kwargs):
        data = self.cleaned_data['amount']
        if data > 3000 or data < 1:
            self.fields['amount'].widget.attrs.update({'autofocus': ''})
            raise forms.ValidationError('amount of library fee can not be > 3000 or < 1')
        return data

    def clean_receipt_date(self, *arg, **kwargs):
        data = self.cleaned_data['receipt_date']
        if data is not None:
            min_date = datetime.date.today() - datetime.timedelta(days=183)
            if data > datetime.date.today() or min_date < data:
                self.fields['receipt_date'].widget.attrs.update({'autofocus': ''})
                raise forms.ValidationError('date cannot be greater than '+str(min_date)+' bro')
        return data
    
    def clean_receipt_no(self, *arg, **kwargs):
        data = self.cleaned_data['receipt_no']
        if data is not None:
            if request_transaction.objects.filter(receipt_no=data).exists():
                self.fields['receipt_no'].widget.attrs.update({'autofocus': ''})
                raise forms.ValidationError('request with receipt number {} already exists'.format(data))
        return data