from django import forms
from users.models import User


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "position": forms.Select(attrs={"class": "form-select"})
        }
