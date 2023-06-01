from django import forms
class studentForm(forms.Form):
    name=forms.CharField()
    mark=forms.IntegerField()
    