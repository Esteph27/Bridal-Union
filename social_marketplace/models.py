from django.db import models
from django.forms import ModelForm
from cloudinary.models import CloudinaryField
from datetime import datetime

# from django.contrib.auth.models import User

# status of images:
STATUS = ((0, "Draft"), (1, "Published"))


# ------> designer model
class Designer(models.Model):
    '''designer model for designer info'''

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    starting_price = models.DecimalField(max_digits=10, decimal_places=5)
    bio = models.TextField()
    bookingref = models.TextField()  # --->placeholder for now, relationship needs to be defined with booking and client model


# ------> image model
class Imageposts(models.Model):
    '''Imageposts model for images posted by Designers'''

    image = CloudinaryField('image', default='placeholder')
    image_description = models.TextField()
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name="imageposts")
    date_posted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(Designer, related_name="imageposts", blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.image_description

    def number_of_like(self):
        return self.likes.count()


# ------> client model
class Customerinfo(models.Model):
    '''customerinfo model for customer informaiton'''

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=245)
    contact_number = models.CharField(max_length=30)  # ---> placeholder for now,
    password = models.CharField(max_length=8)
    budget = models.DecimalField(max_digits=10, decimal_places=5)
    wedding_date = models.DateField()  # ---> placeholder for now,
    bookingref = models.TextField()  # ---> placeholder for now, relationship needs to be defined with booking and client model


# ------> booking modelform
class Bookingform(ModelForm):
    pass

# ------> review model
