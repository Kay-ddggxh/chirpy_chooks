from django.db import models
from django.contrib.auth.models import User

from profiles.models import UserProfile


class EntryType(models.Model):
    """
    Defines type (category) object
    """

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Entry(models.Model):

    class Meta:
        """
        Ensure correct plural of Entry
        in admin UI
        """
        verbose_name_plural = 'Entries'

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    create_date = models.DateField(auto_now_add=True)
    entry_type = models.ForeignKey(
        EntryType, on_delete=models.PROTECT, default=1, related_name="type")
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def get_img_alt_value(self):
        """
        returns descriptive name for alt attribute on entry image
        """
        img_alt_value = self.image.name.replace('-', ' ').split('.', 1)[0]

        return img_alt_value


class Response(models.Model):
    """
    Defines model for response to forum entry
    """
    entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE, related_name='response')
    author = models.CharField(max_length=60)
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f"{self.author} commented on this post"
