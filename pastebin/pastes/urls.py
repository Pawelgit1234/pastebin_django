from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('paste/<slug:slug>/', views.detail, name='detail'),

]