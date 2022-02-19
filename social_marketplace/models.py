from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django_resized import ResizedImageField


class Designer(models.Model):
    '''
    model for designer information
    '''

    # attributes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=245, default='designer@bridal-union.com')
    location = models.CharField(max_length=50)
    starting_price = models.FloatField()
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()

    def __str__(self):
        return self.first_name


class ImagePosts(models.Model):
    '''
    model for images posted by Designer(s)
    '''

    # status of images:
    STATUS = ((0, "Draft"), (1, "Posted"))

    # attributes
    image = CloudinaryField('image', default='placeholder')
    image_description = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)
    date_posted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Related Fiels
    designer = models.ForeignKey(
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
        return f"Posted by {self.designer}"


class ImageComments(models.Model):
    '''
    model for comments on images
    '''

    # attributes
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
        return f"Comment from {self.name}"


class CustomerAccount(models.Model):
    '''
    model for customer account information
    '''

    # attributes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=245)
    contact_number = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=8)
    budget = models.FloatField()
    wedding_date = models.DateField()

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    '''
    model for customer bookings
    '''

    STATUS = (
        ('Upcoming Bookings', 'Upcoming Bookings'),
        ('Past Bookings', 'Past Booking'),
    )

    customer = models.ForeignKey(
        CustomerAccount, null=True, on_delete=models.SET_NULL)
    designer = models.ForeignKey(
        Designer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)



# ------> review model
