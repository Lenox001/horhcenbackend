from rest_framework import serializers
from .models import HomepageContent, AboutSection,GalleryItem,ContactSubmission, SocialMediaLinks,Testimonial


class HomepageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageContent
        fields = '__all__'
class AboutSectionSerializer(serializers.ModelSerializer):
    about_img1 = serializers.SerializerMethodField()
    about_img2 = serializers.SerializerMethodField()
    about_img3 = serializers.SerializerMethodField()

    class Meta:
        model = AboutSection
        fields = '__all__'

    def get_about_img1(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.about_img1.url) if obj.about_img1 else None

    def get_about_img2(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.about_img2.url) if obj.about_img2 else None

    def get_about_img3(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.about_img3.url) if obj.about_img3 else None
    
class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = ["id", "image", "caption", "date_posted"]
        
class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = '__all__'
        
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'