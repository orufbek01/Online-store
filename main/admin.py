from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _



@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ( 'avatar' 'phone_number', 'region')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Size_category)
admin.site.register(Card)
admin.site.register(Saved)
admin.site.register(Order)
admin.site.register(Office)
admin.site.register(Image)