from django import forms
from django.contrib.auth.forms import AuthenticationForm

class PromptForm(forms.Form):
    prompt = forms.CharField(label='Enter a topic or question', max_length=100)
    
class ContentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Paste your content here...'}), required=False)
    pdf = forms.FileField(required=False)
