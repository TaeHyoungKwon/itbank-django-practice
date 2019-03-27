from django.urls import path
from . import views


app_name = "housekeepingbook"

urlpatterns = [
    path('list/', views.hkb_list, name="list"),
    path('create/', views.hkb_create),
    path('<int:id>/', views.hkb_detail, name="detail"),
    path('<int:id>/delete/', views.hkb_delete, name="delete"),
    path('<int:id>/update/', views.hkb_update, name="update")
]
