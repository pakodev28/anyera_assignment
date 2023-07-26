from django.contrib import admin
from django.contrib.auth.models import User

from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "species", "breed", "age")
    list_filter = ("owner", "species", "breed", "age")
    search_fields = ("name", "owner__username")


class PetInline(admin.TabularInline):
    model = Pet
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [PetInline]


admin.site.register(Pet, PetAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
