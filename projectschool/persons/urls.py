
from django.urls import path

from persons import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('persons/demo',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register/register',views.register,name='register'),
    path('login/button',views.person_create_view,name='button'),
    path('login/form',views.form,name='form'),
    path('persons/add', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('login/ajax_load_cities', views.load_cities, name='ajax_load_cities'),  #

]
