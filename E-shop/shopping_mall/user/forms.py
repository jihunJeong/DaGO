from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required':'이메일을 입력해주세요.'
        }, label="이메일", max_length=64)
    
    password = forms.CharField(
        error_messages={
            'required':"비밀번호를 입력해주세요."
        }, label="비밀번호",
        widget=forms.PasswordInput
    )
    re_password = forms.CharField(
        error_messages ={
            'required':"비밀번호를 입력해주세요."
        }, widget = forms.PasswordInput, label="비밀번호 확인"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if User.objects.filter(email=email).exists():
            self.add_error('email', '이미 존재하는 이메일 입니다.')

        if password and re_password:
            if password != re_password :
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required':'이메일을 입력해주세요.'
        }, label="이메일", max_length=64)
    
    password = forms.CharField(
        error_messages={
            'required':"비밀번호를 입력해주세요."
        }, label="비밀번호",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', '존재하지 않는 이메일입니다.')
                return
            if not check_password(password, user.password):
                self.add_error('password', '패스워드가 일치하지 않습니다.')