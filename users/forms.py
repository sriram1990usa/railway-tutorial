from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserLogin(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput())


# class UserRegisterForm(forms.ModelForm):
class UserReg(forms.ModelForm):  
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        # fields = ['username', 'email','email2', 'password' ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserReg, self).clean(*args, **kwargs)


'''
class UserReg(forms.ModelForm):
    number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'number']

    def save(self, commit=True):
        user = super(UserReg, self).save(commit=False)
        user.number = self.cleaned_data["number"]
        if commit:
            user.save()
        return user
'''