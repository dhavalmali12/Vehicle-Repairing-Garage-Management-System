from django import forms

class UsersForms(forms.Form):
    num1=forms.IntegerField, required=False(label="value1",required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    num2=forms.IntegerRangeField,label="value2",required=False,widget=forms.TextInput(attrs={"class":"form-control"})
    # email=forms.EmailField()
    
    
    