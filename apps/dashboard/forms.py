from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
    
        widgets = {
            'text': forms.Textarea(attrs={
                'class':'form-control',
                'rows': 1
            })
        }
