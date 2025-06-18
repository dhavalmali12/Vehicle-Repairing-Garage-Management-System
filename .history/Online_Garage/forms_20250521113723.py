from django import forms

class UserForms(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
    
    