from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:acc_type>', views.index),
    path('income_list/', views.income_list),
    path('expense_list/', views.expense_list),
    path('list/', views.list),
]
