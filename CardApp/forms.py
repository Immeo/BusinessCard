from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    subject = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Тема'}))
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'сообщение'}),)

class SubscribeForm(forms.Form):
    """
    docstring
    """
    SubEemail = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
