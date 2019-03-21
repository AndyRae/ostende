from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import datetime
from PIL import Image


class Home(models.Model):
    home = models.CharField(max_length=50, null=True)


class Venue(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    county = models.CharField(max_length=50, blank=True)
    website = models.URLField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=25, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(default='venue', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('venue-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Film(models.Model):
    CERTIFICATES = [
        ('U', 'U'),
        ('PG', 'PG'),
        ('12A', '12A'),
        ('12', '12'),
        ('15', '15'),
        ('18', '18'),
        ('TBC', 'TBC'),
    ]
    name = models.CharField(max_length=100, null=True)
    director = models.CharField(max_length=50, null=True)
    cast = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=10, null=True)
    certificate = models.CharField(max_length=10, choices=CERTIFICATES, null=True)
    length = models.PositiveIntegerField(null=True)
    copy = models.TextField(max_length=200, null=True)
    image = models.ImageField(default='./media/default.jpg', upload_to='films')
    slug = models.SlugField(default='venue', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('film-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        super(Film, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 1500 or img.width > 1500:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Season(models.Model):
    name = models.CharField(max_length=100, null=True)
    copy = models.TextField(max_length=200, null=True)
    image = models.ImageField(default='./media/default.jpg', upload_to='seasons')
    slug = models.SlugField(default='season', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('season-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Screening(models.Model):
    name = models.CharField(max_length=100, blank=True)
    film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, blank=True, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, blank=True, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    tickets = models.URLField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=50, blank=True)
    q_and_a = models.BooleanField(blank=True)
    slug = models.SlugField(default='venue', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('screening-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)
