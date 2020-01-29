from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import forms

User = get_user_model()

class UserLoginForm(forms.Form): 

    username = forms.CharField(label='Username', label_suffix='', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Username', 'name': '', 'autofocus': 'true'}))
    password = forms.CharField(label='Password', label_suffix='',widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('username')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('User does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        return super(UserLoginForm, self.clean(*args, **kwargs))

class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(label='Email Address', label_suffix='', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Email Address', 'name': '', 'autofocus': 'true'}))
    email2 = forms.CharField(label='Confirm email', label_suffix='', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Email Address', 'name': '', 'autofocus': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data('email')
        email2 = self.cleaned_data('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exist:
            raise forms.ValidationError('This Email already exist')
        return email