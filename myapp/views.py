from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import HomepageContent,AboutSection,GalleryItem,ContactSubmission, SocialMediaLinks,Testimonial
from .serializers import HomepageContentSerializer, AboutSectionSerializer,GalleryItemSerializer,ContactSubmissionSerializer,SocialMediaLinksSerializer,TestimonialSerializer
from rest_framework.generics import ListAPIView

def api_home(request):
    data = {
        "message": "Welcome to the API",
        "status": "success"
    }
    return JsonResponse(data)

class HomepageContentListCreateView(generics.ListCreateAPIView):
    queryset = HomepageContent.objects.all()
    serializer_class = HomepageContentSerializer

class AboutSectionDetailView(generics.RetrieveAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

    def get_object(self):
        return AboutSection.objects.first()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, context={"request": request})
        return Response(serializer.data)
    
class GalleryItemListCreateView(generics.ListCreateAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    
class ContactSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer


class SocialMediaLinksRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = SocialMediaLinks.objects.all()
    serializer_class = SocialMediaLinksSerializer

    def get_object(self):
        return SocialMediaLinks.objects.first()
    
class TestimonialListView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer