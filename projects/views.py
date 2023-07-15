from django.core.paginator import Paginator
from pyquery import PyQuery as pq
from projects.models import Projects
from django.shortcuts import render, get_object_or_404

def projects(request):
    proList = Projects.objects.all().order_by('-publishDate')
    for pro in proList:
        html = pq(pro.description)
        pro.mytxt = pq(html)('p').text()
    p = Paginator(proList, 4)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        proList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(
        request, 'projects.html', {
            'active_menu': 'projects',
            'proList': proList,
            'pageData': pageData,
        })


def projectDetail(request, id):
    mypro = get_object_or_404(Projects, id=id)
    mypro.views += 1
    mypro.save()
    return render(request, 'projectDetail.html', {
        'active_menu': 'projects',
        'mypro': mypro,
    })