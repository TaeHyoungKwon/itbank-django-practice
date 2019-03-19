from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.html_intro),
    path('editor/', views.html_editor)
]
