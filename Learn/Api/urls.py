from django.contrib import admin
from django.urls import path
from Api.views import RegisterView,Loginview,Logoutview,ListUserView
urlpatterns = [
    path('Register/',RegisterView.as_view(), name='Register'),
    path('login/',Loginview.as_view(), name='login'),
    path('logout/',Logoutview.as_view(),name='logout'),
    path('user/',ListUserView.as_view(),name='user'),

]