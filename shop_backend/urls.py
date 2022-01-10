from main import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products', views.get_product),
    path('api/v1/products/<int:id>/', views.get_detail),

]
