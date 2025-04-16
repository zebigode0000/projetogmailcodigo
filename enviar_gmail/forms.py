from django import forms

class CodeVerificationForm(forms.Form):
    code = forms.CharField(label='Código de verificação', max_length=6)
