from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_stock, name='login_stock'),
    path('register/', views.register_stock, name='register_stock'),
    path('logout/', views.logout_stock, name='logout_stock'),
    # Stock CRUD URLs (Class-Based Views)
    path('add/', views.add_stock.as_view(), name='add_stock'),
    path('list/', views.show_stock.as_view(), name='stock_list'),
    path('update/<int:pk>/', views.update_stock.as_view(), name='update_stock'),
    path('delete/<int:pk>/', views.delete_stock.as_view(), name='delete_stock'),
]