from django.contrib import admin
from .models import HomepageContent,AboutSection

@admin.register(HomepageContent)
class HomepageContentAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "feature_title")  # Show these fields in the admin list
    search_fields = ("hero_title", "feature_title")  # Enable searching
    
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