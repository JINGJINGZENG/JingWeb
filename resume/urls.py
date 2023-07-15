from django.urls import path
from . import views

app_name = 'resume'  # 设置应用名

urlpatterns = [
    path('baseinfo/', views.baseinfo, name='baseinfo'),
    path('experience/', views.experience, name='experience'),
    path('proof/', views.proof, name='proof'),
]
