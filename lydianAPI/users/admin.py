from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

class MemberAdmin(UserAdmin):
    model = Member
    fieldsets = UserAdmin.fieldsets
    list_display = ['username', 'email']
    search_fields = ['username', 'email']

admin.site.register(Member, MemberAdmin)