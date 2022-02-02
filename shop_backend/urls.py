from main import views
from django.contrib import admin
from django.conf.urls.static import static
from user import views as user_views
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.ProductCreateListAPIview.as_view()),
    path('api/v1/products/<int:id>/', views.ProductCreateListAPIview.as_view()),
    path('api/v1/products/reviews/', views.ReviewCreateListAPIview.as_view()),
    path('api/v1/products/tags/', views.TagCreateListAPIview.as_view()),
    path('api/v1/login/', user_views.LoginAPIview.as_view()),
    path('api/v1/register/', user_views.RegisterAPIview.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.urls.authtoken')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
