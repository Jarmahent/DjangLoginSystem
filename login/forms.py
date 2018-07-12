from django import forms
from django.contrib.auth.models import User


class CustomUserForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }

    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.")
    email = forms.EmailField(label="Email", max_length=255)
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=100)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    class Meta:
        model = User
        field = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']
        exclude = ['date_joined', 'is_superuser']

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user
