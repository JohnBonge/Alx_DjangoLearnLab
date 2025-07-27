from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BookSearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)
