from django.contrib import admin
from .models import HomepageContent, AboutSection, GalleryItem, ContactSubmission, SocialMediaLinks, Testimonial

@admin.register(HomepageContent)
class HomepageContentAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "feature_title")
    search_fields = ("hero_title", "feature_title")

    fieldsets = (
        ("Hero Section", {
            "fields": ("hero_title", "hero_subtitle", "hero_image1", "hero_image2"),
        }),
        ("Feature Section", {
            "fields": (
                "feature_title", "feature_background",
                "feature1_title", "feature1_description",
                "feature2_title", "feature2_description",
                "feature3_title", "feature3_description"
            ),
        }),
        ("Extra Content", {
            "fields": ("extra_paragraph1", "extra_paragraph2"),
        }),
    )

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "caption", "date_posted")
    ordering = ("-date_posted",)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "submitted_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-submitted_at",)

@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ("instagram", "whatsapp", "facebook", "tiktok")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "title")  # Display name and title in the list view
    search_fields = ("name", "title")  # Enable searching by name and title

    fieldsets = (
        ("Client Info", {
            "fields": ("name", "title"),
        }),
        ("Testimonial", {
            "fields": ("text",),
        }),
    )
