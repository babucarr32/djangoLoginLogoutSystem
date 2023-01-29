
from django.urls import path, include
from .views import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login, name= 'LOGIN'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
