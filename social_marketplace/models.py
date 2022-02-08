from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# status of images:
STATUS = ((0, "Draft"), (1, "Published"))

# gallery model (get images from cloudinary and includes comments)

# client model

# booking model form

# review model

# designer model

class Designer(models.Model):
    '''designer model for designer page'''

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    starting_price = models.DecimalField(max_digits=10, decimal_places=5)
    bio = models.TextField()
