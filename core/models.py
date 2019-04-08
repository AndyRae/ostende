from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from PIL import Image
from tinymce import HTMLField
from datetime import datetime


class Programme(models.Model):
    name = models.CharField(max_length=100, null=True)
    copy = models.TextField(max_length=200, null=True)
    slug = models.SlugField(default='programme', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('programme-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Venue(models.Model):
    name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=10, blank=True)
    county = models.CharField(max_length=50, null=True)
    website = models.URLField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=25, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='venues')
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 1200:
            img.thumbnail((800, 1200), Image.ANTIALIAS)
            img.save(self.image.path, optimize=True)


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
    director = models.CharField(max_length=100, null=True)
    cast = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=10, null=True)
    certificate = models.CharField(max_length=10, choices=CERTIFICATES, null=True)
    length = models.PositiveIntegerField(null=True)
    copy = models.TextField(max_length=1000, null=True)
    image = models.ImageField(default='default.jpg', upload_to='films')
    slug = models.SlugField(default='film', editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('film-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 1200:
            img.thumbnail((800, 1200), Image.ANTIALIAS)
            img.save(self.image.path, optimize=True)


class Season(models.Model):
    name = models.CharField(max_length=100, null=True)
    programme = models.ForeignKey(Programme, null=True, on_delete=models.CASCADE)
    copy = models.TextField(max_length=300, null=True)
    image = models.ImageField(default='default.jpg', upload_to='seasons')
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
    name = models.CharField(max_length=100)
    film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, null=True, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, null=True, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, null=True, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    tickets = models.URLField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=50, blank=True)
    q_and_a = models.BooleanField(blank=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        kwargs = {'pk': self.pk}
        return reverse('screening-detail', kwargs=kwargs)

    def screening_passed(self):
        todaysdate = datetime.now().date()
        if self.date < todaysdate:
            return True


class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    date = models.DateField()
    author = models.CharField(max_length=100, null=True)
    programme = models.ForeignKey(Programme, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='articles')
    text = HTMLField('Text')
    slug = models.SlugField(default='article', editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('article-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)
