from django.http import HttpResponse
from django.shortcuts import render


# 首页
def index_page(request):
    return render(request, 'index.html', {})


# 目录页面
def category_page(request, bookName):
    context = {'bookName': bookName}
    return render(request, 'category.html', context)


def page_not_found(request, e):
    return render(request, '404.html', e)


def page_error(request):
    return render(request, '500.html', {})
