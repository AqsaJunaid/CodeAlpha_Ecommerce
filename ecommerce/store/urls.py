from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('process_order/', views.processOrder, name = "process_order"),
    
    path("login/", views.login_page, name="login_page"), 
    path("logout/", views.logout_page, name="logout_page"), 

    path("register/", views.register_page, name="register_page")


]
