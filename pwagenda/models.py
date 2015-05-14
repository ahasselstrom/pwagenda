from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Meeting(models.Model):
    name = models.CharField(max_length=128, unique=True)
    emails = models.EmailField(help_text="Type emails of participants")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.TimeField(blank=True, null=False, default=timezone.localtime(timezone.now()))
    slug = models.SlugField(unique=True)
    item = models.CharField(unique=False, max_length=250)
    subitem1 = models.CharField(unique=False, max_length=250)
    subitem2 = models.CharField(unique=False, max_length=250)
    subitem3 = models.CharField(unique=False, max_length=250)
    item1 = models.CharField(unique=False, max_length=250)
    subitem4 = models.CharField(unique=False, max_length=250)
    subitem5 = models.CharField(unique=False, max_length=250)
    subitem6 = models.CharField(unique=False, max_length=250)
    item2 = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Meeting, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    company = models.CharField(max_length=158, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
