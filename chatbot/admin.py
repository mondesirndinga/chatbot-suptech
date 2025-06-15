from django.contrib import admin
from .models import Formation, CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'domaine')
    list_filter = ('type', 'domaine')
    search_fields = ('nom', 'mots_cles', 'description')
    ordering = ('type', 'domaine')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'age', 'current_class', 'formation', 'is_staff')
    search_fields = ('username', 'email', 'formation')
    list_filter = ('formation', 'is_staff')
