from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm 
from user.models import *
from django.forms import TextInput, Textarea, EmailInput,FileInput,Select


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "username",
        "id": "username",
        "class" : "contact_form_name input_field",
        "placeholder": "Nhập tên đăng nhập",
    }), label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "class" : "contact_form_email input_field",
        "placeholder": "Nhập địa chỉ email",
    }), label="")
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "first_name",
        "id": "email",
        "class" : "contact_form_name input_field",
        "placeholder": "Nhập họ và đệm",
    }), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "last_name",
        "id": "email",
        "class" : "contact_form_name input_field",
        "placeholder": "Nhập tên",
    }), label="")
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "name": "password1",
        "id": "email",
        "class" : "contact_form_name input_field",
        "placeholder": "Nhập mật khẩu",
    }), label="")
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "name": "password2",
        "id": "email",
        "class" : "contact_form_name input_field",
        "placeholder": "Xác nhận mật khẩu",
    }), label="")

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name','password1','password2',)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','name','address','district','city','name1','address1','district1','city1','image',)
        

class UserUpdateForm(UserChangeForm):
    
    email = forms.EmailField(max_length=100,label='Email ')
    first_name = forms.CharField(max_length=100, label='Họ và đệm')
    last_name = forms.CharField(max_length=100, label='Tên')
    class Meta:
        model = User
        fields = ('email','first_name','last_name',)

class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(max_length=30, label='Điện thoại')

    name = forms.CharField(max_length=100,label='Địa chỉ 1')
    address = forms.CharField(max_length=100,label='Đường, Phường/Xã')
    district = forms.CharField(max_length=100,label='Quận/Huyện')
    city = forms.CharField(max_length=100,label='Thành phố/Tỉnh')

    name1 = forms.CharField(max_length=100,label='Địa chỉ 2')
    address1 = forms.CharField(max_length=100,label='Đường, Phường/Xã')
    district1 = forms.CharField(max_length=100,label='Quận/Huyện')
    city1 = forms.CharField(max_length=100,label='Thành phố/Tỉnh')

    
    
    image = forms.FileField(widget=forms.FileInput(attrs={'accept':'image/*'}),label='Hình ảnh')
    class Meta:
        model = UserProfile
        fields = ('phone','name','address','district','city','name1','address1','district1','city1','image',)


