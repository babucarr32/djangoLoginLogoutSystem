from django.urls import path, include
from .views import signout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signout/', signout, name= 'SIGNOUT'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
