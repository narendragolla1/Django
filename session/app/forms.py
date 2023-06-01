from django import forms
class loginform(forms.Form):
    user_name=forms.CharField( max_length=30, required=False)
    pwd=forms.CharField( max_length=30, required=False)
    