from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import api_home
from .views import HomepageContentListCreateView, AboutSectionDetailView


urlpatterns = [
    path('', api_home, name='api-home'),
     path('homepage/', HomepageContentListCreateView.as_view(), name='homepage-list'),
      path('about/', AboutSectionDetailView.as_view(), name='about-section'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
