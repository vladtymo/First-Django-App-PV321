from django import forms
from users.models import User


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
