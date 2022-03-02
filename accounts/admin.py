from django.contrib import admin
from .models import NewUserDj

# admin.site.register(NewUserDj)


@admin.register(NewUserDj)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_name', 'is_staff', 'join_date')
