from django.db import models

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # This is a link to another model
    title = models.CharField(max_length=200) # This limits how long of a text this can be (For a title)
    text = models.TextField() # This just creates a Text Field with no character limit
    created_date = models.DateTimeField(
            default=timezone.now) # Stores the current Date/Time as the created_date
    published_date = models.DateTimeField(
            blank=True, null=True) # Stores the published_date as null for now

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
