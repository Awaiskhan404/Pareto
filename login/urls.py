from django.urls import path
from login import views



urlpatterns = [
   
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('auth',views.handle_login,name="auth"),
    path('auth_signup',views.handle_signup,name="auth_signup"),
    path('logout',views.logout,name="logout"),
    path('dashboard/logout',views.logout,name="logout")
    
    
]
