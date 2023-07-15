from django.shortcuts import render

from projects.models import Projects
from resource.models import Resource


def home(request):
    proList = Projects.objects.all().order_by('-publishDate')
    if(len(proList)>3):
        proList = proList[0:3]
    resList = Resource.objects.all().order_by('-publishDate')
    if (len(resList) > 3):
        resList = resList[0:3]
    return render(request, 'home.html', {
        'active_menu': 'home',
        'proList': proList,
        'resList': resList,
    })
