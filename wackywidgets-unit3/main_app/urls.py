from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('widgets/add_widget/', views.add_widget, name='add_widget'),
]
