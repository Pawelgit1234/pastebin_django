from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]
