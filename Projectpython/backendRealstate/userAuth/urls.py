from django.contrib import admin
from django.urls import path , include

from . import views
from .views import RegisterView,LoginView,UserView,LogoutView

urlpatterns = [
    path('role-create/', views.create_role, name='role-create'),
    path('role-update/<int:pk>/', views.update_role, name='role-update'),
    path('role-delete/<int:pk>/', views.delete_role, name='role-delete'),

    path('user-create/', views.create_user, name='user-create'),
    path('user-update/<int:pk>/', views.updateUser, name='user-update'),
    path('user-delete/<int:pk>/', views.deleteUser, name='user-delete'),
    path('user-search/<int:pk>/', views.searchUserById, name='user-search-by-id'),
    path('users/', views.list_users, name='list-users'),

    path('api/register', RegisterView.as_view()),
    path('api/login', LoginView.as_view()),
    path('api/user', UserView.as_view()),
    path('api/logout', LogoutView.as_view()),

    path('temoinage-create/', views.create_temoinage, name='temoinage-create'),
    path('temoinage-update/<int:pk>/', views.update_temoinage, name='temoinage-update'),
    path('temoinage-delete/<int:pk>/', views.delete_temoinage, name='temoinage-delete'),
    path('temoinages/', views.list_temoinages, name='list-temoinages'),
    path('temoinage-search/<int:pk>/', views.searchTemoinageById, name='temoinage-search-by-id'),

    path('blog-create/', views.create_blog, name='blog-create'),
    path('blog-update/<int:pk>/', views.update_blog, name='blog-update'),
    path('blog-delete/<int:pk>/', views.delete_blog, name='blog-delete'),
    path('blogs/', views.list_blogs, name='list-blogs'),
    path('blog-search/<int:pk>/', views.searchBlogById, name='blog-search-by-id'),

    path('contact-create/', views.create_contact, name='contact-create'),
    path('contact-update/<int:pk>/', views.update_contact, name='contact-update'),
    path('contact-delete/<int:pk>/', views.delete_contact, name='contact-delete'),
    path('contacts/', views.list_contacts, name='list-contacts'),
    path('contact-search/<int:pk>/', views.searchContactById, name='contact-search-by-id'),
]