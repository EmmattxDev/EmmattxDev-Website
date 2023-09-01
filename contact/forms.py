from django import forms
from django.core.validators import EmailValidator
from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,required=True, widget=forms.TextInput(
        attrs={
            'placeholder': 'First name',
            'id': 'first_name'
        }
    ))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={
            'placeholder': 'Last name', 
            'id': 'last_name'
        }
    ))
    email = forms.EmailField(required=True,       validators=[EmailValidator()], 
        widget=forms.EmailInput(
        attrs={
            'placeholder': 'Your Email',
            'id': 'email'
        }
    ))
    subject = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Subject',
            'id': 'subject'
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
                'cols': 15,
               'rows': 8,
               'placeholder': 'Message Here...',
               'required': True
               }
    ))

    class Meta:
        model = Contact
        fields = '__all__'



