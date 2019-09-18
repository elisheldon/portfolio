from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label = _('Username'))
    password = forms.CharField(label = _('Password'), widget = forms.PasswordInput)

class RegistrationForm(forms.Form):
    username = forms.CharField(label = _('Username'))
    firstName = forms.CharField(label = _('First name'))
    lastName = forms.CharField(label = _('Last name'))
    email = forms.EmailField(label = _('Email address'))
    userTypeChoices = (('student',_('Student')),('teacher',_('Teacher')))
    userType = forms.ChoiceField(label = _('I am a...'), choices = userTypeChoices)
    password1 = forms.CharField(label = _('Password'), widget = forms.PasswordInput)
    password2 = forms.CharField(label = _('Confirm password'), help_text=_('Enter the same password as above, for verification.'), widget = forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_('This username is already in use, please try another.'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_('This email address is already associated with an account.'))

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(
                _('Passwords do not match.'),
            )
        return password2