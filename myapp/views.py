from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import HomepageContent,GalleryItem,ContactSubmission, SocialMediaLinks,SafariPackage,Destination
from .serializers import HomepageContentSerializer, GalleryItemSerializer,ContactSubmissionSerializer,SocialMediaLinksSerializer,SafariPackageSerializer,DestinationSerializer
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
    

    
class SafariPackageListView(generics.ListCreateAPIView):
    """
    List all safari packages or create a new one.
    """
    queryset = SafariPackage.objects.all()
    serializer_class = SafariPackageSerializer

class SafariPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a safari package by slug.
    """
    queryset = SafariPackage.objects.all()
    serializer_class = SafariPackageSerializer
    lookup_field = "slug"


    
class DestinationListView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = "slug"