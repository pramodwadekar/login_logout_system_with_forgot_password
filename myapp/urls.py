from django.urls import path, include
from .import views

urlpatterns = [
    path("",views.Register_page, name = 'register_page'),
    path('register/', views.User_Register, name = "register"),
    path("loginpage/", views.loginpage, name = "loginpage"),
    path("loginuser/", views.LoginUser, name = "login"),
    path("fpassword/", views.forgot_pass, name = "forgot"),
    path('change_pass/', views.fpassword, name = "fpassword"),
    
    path("index/",views.index, name = 'index'),
    path("chart/", views.pie_chart, name = 'chart'),
    path("filterbyname/", views.filter_data, name = 'name'),
    
]