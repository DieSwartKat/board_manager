from typing_extensions import ParamSpecArgs
from django.contrib import admin
from .models import Role, Member, Board, Board_Member_Role

# Register your models here.

@admin.register(Role, Member, Board, Board_Member_Role)
class RoleAdmin(admin.ModelAdmin):
    pass