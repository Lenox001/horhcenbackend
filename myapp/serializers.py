from rest_framework import serializers
from .models import HomepageContent, GalleryItem,ContactSubmission, SocialMediaLinks,SafariPackage, ItineraryDay,Destination


class HomepageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageContent
        fields = '__all__'

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = ["id", "image", "alt_text", "date_posted"]  # Updated 'caption' → 'alt_text'
        
class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = '__all__'
        

        




class ItineraryDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryDay
        fields = ["day_number", "description"]

class SafariPackageSerializer(serializers.ModelSerializer):
    itinerary = ItineraryDaySerializer(many=True, read_only=True)

    class Meta:
        model = SafariPackage
        fields = [
            "title", "description", "location", "duration", "price", "max_people",
            "slug", "reviews_count", "rating", "image", "itinerary"  # Added image field
        ]
        lookup_field = "slug"

class DestinationSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:  # Ensure there's an image before trying to format the URL
            request = self.context.get("request")  # Get the request object if available
            return request.build_absolute_uri(obj.image.url) if request else f"{settings.MEDIA_URL}{obj.image}"
        return None  # Return None if no image is available

    class Meta:
        model = Destination
        fields = ["title", "country", "image", "description", "rating", "slug"]