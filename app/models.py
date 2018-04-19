from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class NullHydFollower(models.Model):
    follower_name = models.CharField(max_length=30)
    registration_date = models.DateField(default=datetime.date.today)

    def __str__(self):  # __unicode__ on Python 2
        return self.follower_name


@python_2_unicode_compatible
class Comment(models.Model):
    content = models.CharField(max_length=500, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
