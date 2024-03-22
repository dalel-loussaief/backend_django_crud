
from django.urls import path , include
from . import views
urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),
    path('property-list/', views.ShowAll, name='property-list'),
    path('property-detail/<int:pk>/', views.ViewProperty, name='property-detail'),
    path('property-create/', views.CreateProperty, name='property-create'),
    path('property-update/<int:pk>/', views.updateProperty, name='property-update'),
    path('property-delete/<int:pk>/', views.deleteProperty, name='property-delete'),
    path('property-search/<int:pk>/', views.searchPropertyById, name='property-search-by-id'),

    path('Show/', views.Show, name='show_category'),
    path('category-detail/<int:pk>', views.ViewCategory, name='category_detail'),
    path('category-create/', views.CreateCategory, name='category-create'),
    path('category-update/<int:pk>/', views.updateCategory, name='category-update'),
    path('category-delete/<int:pk>/', views.deleteCategory, name='category-delete'),
    path('category-search/<int:pk>/', views.searchCategoryById, name='category-search-by-id'),

    path('createImage/', views.createImage, name='create_image'),
    path('updateImage/<int:pk>/', views.updateImage, name='image-update'),
    path('deleteImage/<int:pk>/', views.deleteImage),
]