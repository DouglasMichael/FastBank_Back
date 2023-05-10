from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")

admin.site.register(Usuario, ProfileAdmin)