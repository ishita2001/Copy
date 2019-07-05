from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'web'

urlpatterns = [
    path('buyersignup/', views.buyer_signup_view, name='buyer_signup'), 
    path('sellersignup/', views.seller_signup_view, name='seller_signup'),
    path('login/', views.login_view , name='login'), 
    path('loggedin/', views.login_index , name='login_index'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name="home"),
    path('options/', views.signup_options,name="signup_options"),
    path('myprofile/',views.my_profile,name="my_profile"),
    path('myprofile/edit/',views.edit_profile,name="edit_profile"),
    path('myprofile/password/',views.change_password,name="change_password"),
    path('search/',include('haystack.urls')),
    path('product/(?P<pk>\d+)/',views.product,name="product"),
]