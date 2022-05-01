from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ShopListView, ShopCreateView, ShopUpdateView, ShopDeleteView, upload_file
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop/new/', ShopCreateView.as_view(), name='shop-create'),
    path('shop/<int:pk>/update/', ShopUpdateView.as_view(), name='shop-update'),
    path('shop/<int:pk>/delete/', ShopDeleteView.as_view(), name='shop-delete'),
    path('list/', views.upload_file, name='list')
]
