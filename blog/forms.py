from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=50)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea, max_length=600)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=250)
