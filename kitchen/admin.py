from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Dish, Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = (
        ("Additional info", {"fields": ("years_of_experience",)}),
    ) + UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "dish_type"]
    list_filter = ["dish_type"]
    search_fields = ["name"]


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
