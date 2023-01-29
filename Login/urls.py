
from django.urls import path, include
from .views import login, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login, name= 'LOGIN'),
    path('logout/', logout, name= 'LOGOUT'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
