from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.loginPage, name="login")
]