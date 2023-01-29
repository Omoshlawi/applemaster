from django.contrib import admin

# Register your models here.
from .models import UserProfile, ResidentialInfo


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'description', 'phone')
    list_filter = ('user', 'description', 'phone')
    search_fields = ('user', 'description', 'phone')
    raw_id_fields = ('user',)


@admin.register(ResidentialInfo)
class ResidentialInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'zip_code', 'apartment_or_floor', 'country', 'postal_code')
    list_filter = ('user', 'address', 'city', 'zip_code', 'apartment_or_floor', 'country', 'postal_code')
    search_fields = ('user', 'address', 'city', 'zip_code', 'apartment_or_floor', 'country', 'postal_code')
    raw_id_fields = ('user',)
