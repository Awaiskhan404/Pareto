from django.urls import path
from login import views



urlpatterns = [
   
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup")
    
]
