from django import forms
from .models import User,Session_Schedule


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)



class SignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__iexact=email).first()
        if user:
            if user.is_staff:
                user_role = "Staff"

            else:
                user_role = "Mentor"
            raise forms.ValidationError(
                "{} with this email already exists, use another email.".format(
                    user_role
                )
            )
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError("Password should be minimum 6 characters long")

        if password != self.data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")
        return password

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session_Schedule
        fields = ('session_name','session_location')




NUMS= [
    ('present', 'present'),
    ('late', 'late'),
    ('absent', 'absent'),
    ]
class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))