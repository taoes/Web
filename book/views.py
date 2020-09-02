from django.http import HttpResponse


def demo1_index(request):
    return HttpResponse("<h1>book/index</h1>")
