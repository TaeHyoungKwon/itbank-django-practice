from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('tag/<int:tag_id>/', views.tag_example),
    path('test_file_io/', views.test_file_io),
    path('html_link/', views.html_link)
]
