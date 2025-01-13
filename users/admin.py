from django.contrib import admin

from users.forms import UserForm
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "birthdate", "username", "position")
    search_fields = ("name", "email", "username")
    list_filter = ("position",)
    exclude = ['username']
    form = UserForm

# Register your models here.
admin.site.register(User, UserAdmin)