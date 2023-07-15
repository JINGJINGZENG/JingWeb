from django.urls import path
from . import views

app_name = 'resource'  # 设置应用名

urlpatterns = [
    path('resource/', views.resource, name='resource'),
    path('resourceDetail/<int:id>/', views.resourceDetail, name='resourceDetail'),
]
