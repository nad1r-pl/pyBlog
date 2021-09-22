"""Define the Database models for this application."""
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from preferences.models import Preferences


class Blog(models.Model):
    """Define the blog model.

    This will contain individual blog entries.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    slug = models.SlugField(default="", unique=True)

    class Meta:
        """Meta configuration for the Blog model."""

        ordering = ["-created_at"]

    def __str__(self):
        """Return string representation of the Blog object."""
        return self.title

    def save(self, *args, **kwargs):
        """Override the save fumction, so we can generate the slug."""
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])


class SitePreferences(Preferences):
    """Define the global site settings."""

    sitename = models.CharField(max_length=50, default="My Sexy Blog")
    title = models.CharField(max_length=20, default="My Blog")
    heading = models.CharField(
        max_length=200, default="A blog of blogging blogosity."
    )

    class Meta:
        """class-specific configuration."""

        verbose_name_plural = "Site Preferences"
