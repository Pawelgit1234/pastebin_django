from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]
