from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import api_home
from .views import HomepageContentListCreateView,GalleryItemListCreateView,ContactSubmissionCreateView, SocialMediaLinksRetrieveUpdateView,SafariPackageListView, SafariPackageDetailView,DestinationListView, DestinationDetailView


urlpatterns = [
    path('', api_home, name='api-home'),
     path('homepage/', HomepageContentListCreateView.as_view(), name='homepage-list'),
     
      path("gallery/", GalleryItemListCreateView.as_view(), name="gallery-list-create"),
       path("contact/", ContactSubmissionCreateView.as_view(), name="contact-create"),
    path("social-media/", SocialMediaLinksRetrieveUpdateView.as_view(), name="social-media"),
    
     path("safaris/", SafariPackageListView.as_view(), name="safari-list"),
    path("safaris/<slug:slug>/", SafariPackageDetailView.as_view(), name="safari-detail"),
     path("destinations/", DestinationListView.as_view(), name="destination-list"),
    path("destinations/<slug:slug>/", DestinationDetailView.as_view(), name="destination-detail"),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
