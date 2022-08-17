from django.urls import path
from dashboard import views

urlpatterns = [
    path('dashboard/', views.home,name='home'),
    path('add/',views.add,name='add'),
    path('addMovie/',views.addMovie,name='addMovie'),
    path('logout',views.logoutPage,name='logout'),
]
