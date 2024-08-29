from django.contrib import admin

from .models import User, Role


class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'role')


admin.site.register(User, UserAdmin)
admin.site.register(Role)