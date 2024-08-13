from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path('sign-up/', views.Register, name='sign-up'),
    path('sign-in/', views.Login, name='sign-in'),
    path('sign-out/', views.Logout, name='sign-out'),
]