from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("response complete")


def blog(request):
    return HttpResponse("블로그 앱!!")


def html(request):
    return HttpResponse('HTML 학습')
