from django import forms


class SendForm(forms.Form):
    name = forms.CharField(label='',  required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='',  required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    subject = forms.CharField(label='',  required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Тема'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'сообщение'}), required=True, )
