from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "tekrar şifre girin", "class": "form-control" }))

    class Meta:
        model = Account
        fields = ["first_name", "last_name", "phone_number", "email", "password"]

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")

        if password != confirm_password:
            raise forms.ValidationError("şifre eşleşmiyor")


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"]
        self.fields["last_name"]
        self.fields["phone_number"]
        self.fields["email"]
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
