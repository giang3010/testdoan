from django import forms
from django.forms import TextInput, Textarea

from .models import ContactMessage, Subscribe

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name','email','phone','message')
        widgets = {
            'name' : TextInput(attrs={'class' : 'input','placeholder' : 'Tên'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Điện thoại'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Tin nhắn','rows':'5'}),
        }


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "class" : "newsletter_input",
        "placeholder": "Nhập địa chỉ email",
    }), label="")

    class Meta:
        model = Subscribe
        fields = ('email', )
        