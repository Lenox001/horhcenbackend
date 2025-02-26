from django.db import models

class HomepageContent(models.Model):
    # Hero Section
    hero_title = models.CharField(
        max_length=255, 
        help_text="Main hero title.", 
        blank=False, 
        null=False, 
        default="Discover Safari Wonders with Horchen Africa"
    )
    hero_subtitle = models.TextField(
        help_text="Hero section subtitle.", 
        blank=False, 
        null=False, 
        default="Experience breathtaking landscapes, luxury safari lodges, and unforgettable wildlife adventures."
    )
    hero_image1 = models.ImageField(
        upload_to="hero/", 
        help_text="First hero image.", 
        blank=False, 
        null=False
    )
    hero_image2 = models.ImageField(
        upload_to="hero/", 
        help_text="Second hero image.", 
        blank=False, 
        null=False
    )

    # Feature Section (Text Editable, Icons & Play Button Fixed)
    feature_title = models.CharField(
        max_length=255, 
        help_text="Main feature section title.", 
        blank=False, 
        null=False, 
        default="Experience the Wild Like Never Before"
    )
    
    feature_background = models.ImageField(
        upload_to="features/", 
        help_text="Feature section background image.", 
        blank=False, 
        null=False
    )

    feature1_title = models.CharField(
        max_length=100, 
        help_text="Title for first feature.", 
        blank=False, 
        null=False, 
        default="Sustainable Safaris"
    )
    feature1_description = models.TextField(
        help_text="Description for first feature.", 
        blank=False, 
        null=False, 
        default="Eco-friendly experiences that preserve wildlife and protect the natural beauty of Africa."
    )

    feature2_title = models.CharField(
        max_length=100, 
        help_text="Title for second feature.", 
        blank=False, 
        null=False, 
        default="Expert Local Guides"
    )
    feature2_description = models.TextField(
        help_text="Description for second feature.", 
        blank=False, 
        null=False, 
        default="Discover hidden gems and iconic landscapes with experienced guides who know every corner of the wild."
    )

    feature3_title = models.CharField(
        max_length=100, 
        help_text="Title for third feature.", 
        blank=False, 
        null=False, 
        default="Luxury in the Wild"
    )
    feature3_description = models.TextField(
        help_text="Description for third feature.", 
        blank=False, 
        null=False, 
        default="Enjoy the perfect blend of adventure and comfort with our handpicked safari lodges and camps."
    )

    # Extra Paragraphs (Now Editable)
    extra_paragraph1 = models.TextField(
        help_text="First extra paragraph.", 
        blank=False, 
        null=False, 
        default="From thrilling game drives to tranquil sunset safaris, Horchen Africa ensures an unforgettable adventure in the wild."
    )
    
    extra_paragraph2 = models.TextField(
        help_text="Second extra paragraph.", 
        blank=False, 
        null=False, 
        default="Join us as we explore the vast beauty of Africa, guided by experts who bring every safari to life."
    )

    def __str__(self):
        return "Homepage Content"

class AboutSection(models.Model):
    title = models.CharField(max_length=255, default="Horchen Africa Safaris", null=True, blank=True)
    subtitle = models.CharField(max_length=255, default="Discover Africa’s Untamed Beauty", null=True, blank=True)
    description = models.TextField(default="Experience the thrill of the wild with Horchen Africa Safaris.", null=True, blank=True)

    about_img1 = models.ImageField(upload_to="about/", null=True, blank=True)
    about_img2 = models.ImageField(upload_to="about/", null=True, blank=True)
    about_img3 = models.ImageField(upload_to="about/", null=True, blank=True)

    def __str__(self):
        return self.title or "About Section"
    

class GalleryItem(models.Model):
    image = models.ImageField(upload_to="gallery_images/")
    caption = models.TextField(blank=True)
    date_posted = models.DateTimeField()

    class Meta:
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return f"Gallery Item {self.id}"
    
    

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

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.title}"