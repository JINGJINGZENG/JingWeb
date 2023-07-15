from django.urls import path
from . import views

app_name = 'projects'  # 设置应用名

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('projectDetail/<int:id>/', views.projectDetail, name='projectDetail'),
]
