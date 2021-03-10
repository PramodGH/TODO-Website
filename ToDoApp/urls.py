
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('add-todo/', views.addtodo, name='addtodo'),
    path('delete-todo/<int:id>/', views.deletetodo, name='delete-todo')

]
