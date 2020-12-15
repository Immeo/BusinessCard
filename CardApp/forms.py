from django import forms


class SendForm(forms.Form):
    name = forms.CharField(label='Имя',  required=True, )
    email = forms.EmailField(label='Email',  required=True, )
    subject = forms.CharField(label='Тема',  required=True, )
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(), required=True, )

    