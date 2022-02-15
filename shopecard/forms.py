from django import forms




class  ItemForm(forms.Form):
    name=forms.CharField()
    quality=forms.CharField()
