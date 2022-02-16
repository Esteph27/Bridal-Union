from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django_resized import ResizedImageField

# status of images:
STATUS = ((0, "Draft"), (1, "Posted"))


class Designer(models.Model):
    '''
    model for designer information
    '''

    # field variables
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    starting_price = models.DecimalField(max_digits=10, decimal_places=5)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()

    def __str__(self):
        return self.first_name


class ImagePosts(models.Model):
    '''
    model for images posted by Designer(s)
    '''

    # field variables
    image = CloudinaryField('image', default='placeholder')
    image_description = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)
    date_posted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Related Fiels
    designer_name = models.ForeignKey(
        Designer, null=True, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='imagepost_like', blank=True)

    # helpers
    class Meta:
        '''
        class to order images posted by most recent
        '''
        ordering = ['-date_posted']

    def number_of_likes(self):
        '''
        function to get number of likes
        '''
        return self.likes.count()

    def __str__(self):
        return f"{self.image_description} by {self.designer_name}"


class ImageComments(models.Model):
    '''
    model for comments on images
    '''

    # field variables
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # related field
    post = models.ForeignKey(
        ImagePosts, on_delete=models.CASCADE, related_name="comments")

    # helpers
    class Meta:
        '''
        order comments by most recent 
        '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class CustomerAccountInfo(models.Model):
    '''
    model for customer account information
    '''

    # field variables
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=245)
    contact_number = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    budget = models.DecimalField(max_digits=10, decimal_places=5)
    wedding_date = models.DateField()

    # related fields
    # bookingref = models.TextField()




# ------> review model
