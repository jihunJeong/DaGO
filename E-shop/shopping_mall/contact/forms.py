from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    email = forms.EmailField(initial='',
        error_messages={
            'required': "이메일을 입력해주세요."
        }, label="Email", max_length=20,
    )

    name = forms.CharField(
        error_messages={
            'required': "이름을 입력해주세요."
        }, label="Name",
        widget=forms.TextInput
    )

    phonenumber = forms.CharField(
        error_messages={
            'required': "전화번호를 입력해주세요."
        }, label="Phone Number",
        widget=forms.NumberInput
    )

    message = forms.CharField(
        error_messages={
            'required': "메세지을 입력해주세요."
        }, label="Message",
        widget=forms.TextInput(attrs={'class': 'message-box'})
    )

    class Meta:
        model = Contact
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['message'].widget.attrs = {
    #         # 'class': 'message-box',
    #         'size': 5
    #     }