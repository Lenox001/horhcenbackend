from django.db import models
from django.utils.text import slugify


class HomepageContent(models.Model):
    # Hero Section
    hero_title = models.CharField(
        max_length=255,
        help_text="Main hero title.",
        blank=False,
        null=False,
        default="Explore the World with Us"
    )
    hero_text = models.TextField(
        help_text="Hero section description.",
        blank=False,
        null=False,
        default="Discover breathtaking destinations, immerse yourself in diverse cultures, and create unforgettable memories. Your next adventure starts here!"
    )

    def __str__(self):
        return "Homepage Content"



    
    

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class SocialMediaLinks(models.Model):
    instagram = models.URLField(default="https://instagram.com")
    whatsapp = models.URLField(default="https://wa.me")
    facebook = models.URLField(default="https://facebook.com")
    tiktok = models.URLField(default="https://tiktok.com")

    def __str__(self):
        return "Social Media Links"

class GalleryItem(models.Model):
    image = models.ImageField(upload_to="gallery_images/")
    alt_text = models.CharField(max_length=255, default="Gallery image")  # Matches <img alt="">
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_posted"]
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return f"Gallery Item {self.id} - {self.date_posted.strftime('%Y-%m-%d')}"
    
from django.db import models
from django.utils.text import slugify

class SafariPackage(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_people = models.PositiveIntegerField(null=True, blank=True)  # Maximum people allowed
    reviews_count = models.PositiveIntegerField(default=0)  # Reviews count field
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)  # Rating field
    image = models.ImageField(upload_to="safari_packages/", null=True, blank=True)  # Added image field
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ItineraryDay(models.Model):
    safari = models.ForeignKey(SafariPackage, related_name="itinerary", on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    description = models.TextField()


class Destination(models.Model):
    title = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, help_text="Country where the destination is located.", blank=True, null=True)
    image = models.ImageField(upload_to="destination_images/", blank=True, null=True)
    description = models.TextField(help_text="Short description of the destination.", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5, help_text="Rating out of 5 stars.", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title