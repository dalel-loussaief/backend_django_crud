from django.urls import path
from . import views

urlpatterns = [
    #path('',views.apiOverview, name='apiOverview'),
    path('service-list/', views.ShowAll, name='service-list'),
    path('service-detail/<int:pk>/', views.ViewService, name='service-detail'),
    path('service-create/', views.CreateService, name='service-create'),
    path('service-update/<int:pk>/', views.updateService, name='service-update'),
    path('service-delete/<int:pk>/', views.deleteService, name='service-delete'),
    path('service-search/<int:pk>/', views.searchServiceById, name='service-search-by-id'),

]