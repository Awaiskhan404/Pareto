from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('explore',views.services,name="services"),
   
    # path('url',views.randoms,name="url")
]
