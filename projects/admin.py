from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    style_fields = {'description':'ueditor'}

admin.site.register(Projects, ProjectsAdmin)