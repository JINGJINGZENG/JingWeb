from django.contrib import admin

# Register your models here.
from resume.models import Proof


class ProofAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']

admin.site.register(Proof,ProofAdmin)
admin.site.site_header = '曾晶晶的个人网站后台管理系统'
admin.site.site_title = '曾晶晶的个人网站后台管理系统'
