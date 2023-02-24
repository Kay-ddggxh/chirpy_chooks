from django.db import models


class EntryType(models.Model):
    """
    Defines tag (category) object
    """
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Entry(models.Model):
    """
    Defines Haiku object
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    entry_type = models.ForeignKey(
        EntryType, on_delete=models.PROTECT, default=1, related_name="type")

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title
