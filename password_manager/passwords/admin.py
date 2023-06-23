from django.contrib import admin
from .models import Category, PasswordGroup, Password, PasswordShare, Profile

admin.site.register(Category)
admin.site.register(PasswordGroup)
admin.site.register(Password)
admin.site.register(PasswordShare)
admin.site.register(Profile)
