from django.contrib import admin
from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    style_fields = {'description':'ueditor'}

admin.site.register(Resource, ResourceAdmin)