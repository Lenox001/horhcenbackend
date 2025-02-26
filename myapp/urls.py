from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import api_home
from .views import HomepageContentListCreateView, AboutSectionDetailView,GalleryItemListCreateView,ContactSubmissionCreateView, SocialMediaLinksRetrieveUpdateView,TestimonialListView


urlpatterns = [
    path('', api_home, name='api-home'),
     path('homepage/', HomepageContentListCreateView.as_view(), name='homepage-list'),
      path('about/', AboutSectionDetailView.as_view(), name='about-section'),
      path("gallery/", GalleryItemListCreateView.as_view(), name="gallery-list-create"),
       path("contact/", ContactSubmissionCreateView.as_view(), name="contact-create"),
    path("social-media/", SocialMediaLinksRetrieveUpdateView.as_view(), name="social-media"),
     path('testimonial/', TestimonialListView.as_view(), name='testimonial-list'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
