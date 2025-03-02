from django.contrib import admin
from .models import HomepageContent,  GalleryItem, ContactSubmission, SocialMediaLinks,SafariPackage,  ItineraryDay,Destination

@admin.register(HomepageContent)
class HomepageContentAdmin(admin.ModelAdmin):
    list_display = ("hero_title",)  # Removed `feature_title`
    search_fields = ("hero_title",)

    fieldsets = (
        ("Hero Section", {
            "fields": ("hero_title", "hero_text"),
        }),
    )



@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "alt_text", "date_posted")  # Updated 'caption' → 'alt_text'
    ordering = ("-date_posted",)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "submitted_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-submitted_at",)

@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ("instagram", "whatsapp", "facebook", "tiktok")



class ItineraryDayInline(admin.TabularInline):
    model = ItineraryDay
    extra = 1  # Allows adding multiple itinerary days inside SafariPackage

@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "duration", "price", "max_people", "image"]
    search_fields = ["title", "location"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItineraryDayInline]

admin.site.register(ItineraryDay)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("title", "country", "rating", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "country", "description")