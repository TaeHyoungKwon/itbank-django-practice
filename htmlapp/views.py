'''
views.py
'''
from django.shortcuts import render


def html_intro(request):
    '''
    html_intro
    '''
    return render(request, 'html/html_editor.html')


def html_editor(request):
    '''
    html_editor
    '''
    return render(request, 'html/html_intro.html')


def test(request):
    '''
    html_editor
    '''
    return render(request, 'html/index.html')
