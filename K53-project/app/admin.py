from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Category, Question, Choice, Answer, TestNumber


User = get_user_model()

class CustomUserAdmin(UserAdmin):
    exclude = ('password_authentication_enabled',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Licence Info', {'fields': ('licence_type', 'licence_code')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(TestNumber)
