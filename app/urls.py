from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/', views.delete_image, name='delete_image'), 
    
    # Add more URL patterns as needed
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
