from django.contrib import admin
from .models import Profile
# Register your models here.


# @admin.register(Profile)
# class ProfileInfo(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', 'image']
#     raw_id_fields = ['user']
admin.site.register(Profile)
