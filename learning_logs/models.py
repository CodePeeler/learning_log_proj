import os

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model. """
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string rep of the model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return f"{self.text[:50]}"


class Image(models.Model):
    img_type = models.CharField(max_length=100, default='sample')
    img_class = models.CharField(max_length=100, default='unclassified')
    img_dir = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation the type of model. """
        return f"{self.id}_{self.img_dir.name.split('/')[-1]}"


#  Clean-up, delete image file on delete of Image instances.
@receiver(pre_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    # Check if the image field has a value
    if instance.img_dir:
        # Get the path of the image file
        image_path = instance.img_dir.path
        # Check if the image file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)
