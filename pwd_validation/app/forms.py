from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    username=forms.CharField()
    pwd=forms.CharField()
    re_pwd=forms.CharField()
    
    def clean(self):
        total_cleaned_data=super().clean()
        psd1=total_cleaned_data['pwd']
        psd2=total_cleaned_data['re_pwd']
        
        if psd1!=psd2:
            raise forms.ValidationError('Both the PASWORD show be same.!')
        elif len(psd1)<8:
            raise forms.ValidationError('Password should be more than 8 Characters')
        elif psd1 not in ['@','!','#']:
            raise forms.ValidationError('Password should contain atleast one of !, @, #')
        