from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', views.account_info, name='account_info'),
]
