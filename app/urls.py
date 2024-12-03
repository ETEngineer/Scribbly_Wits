from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('create/', views.post, name='post'),
    path('logout/', views.logout_view, name='logout'),
    path('myblogs/', views.my_blogs, name='myblogs')
]