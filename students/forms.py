from django import forms
from .models import StudentsInfo

class studentForm(forms.ModelForm):
    class Meta:
        model = StudentsInfo
        fields  = ['name','email','phone_number','course']


    def clean_phone_number(self):
            phone = self.cleaned_data.get('phone_number')
            if StudentsInfo.objects.filter(phone_number=phone).exclude(id=self.instance.id).exists():
                raise forms.ValidationError('This phone number is already taken. Please use a different one.')
            return phone

    def clean_email(self):
            email = self.cleaned_data.get('email')
            if StudentsInfo.objects.filter(email=email).exclude(id=self.instance.id).exists():
                raise forms.ValidationError('This email is already taken. Please use a different one.')
            return email