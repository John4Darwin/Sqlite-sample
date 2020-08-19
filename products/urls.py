from django.urls import path
from . import views
urlpatterns = [
    path("", views.log, name='home'),
   path('index2/', views.new,name='index2'),
   path('contact/', views.con, name='contact'),
   path('index/', views.index, name='index'),
   path('logout/', views.user_logout, name='logout')
]