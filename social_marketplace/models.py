from datetime import datetime 
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Designer(models.Model):
    '''
    A model to store designer information
    '''

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(
        max_length=245,
        default='designer@bridal-union.com')
    location = models.CharField(max_length=50)
    starting_price = models.FloatField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()

    def __str__(self):
        return self.first_name


class ImagePosts(models.Model):
    '''
    A model to store and display images posted by Designer(s)
    '''

    # status of images:
    STATUS = ((0, "Draft"), (1, "Posted"))

    image = CloudinaryField(
        'image',
        default='placeholder',
        transformation={
            'gravity': 'center', 'height': 1000, 'width': 1000, 'crop': 'fit'},
        )
    image_name = models.CharField(max_length=30, default='name of image')
    image_description = models.TextField(null=True, blank=True)
    hashtags = models.CharField(max_length=300, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # related Fields
    designer = models.ForeignKey(
        Designer, null=True, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='imagepost_like', blank=True)

    class Meta:
        '''
        order images posted by most recent
        '''
        ordering = ['-date_posted']

    def number_of_likes(self):
        '''
        get number of likes
        '''
        return self.likes.count()

    def __str__(self):
        return f"{self.image_name} posted by {self.designer}"


class ImageComments(models.Model):
    '''
    A model to store and handle User comments on a designer's post
    '''

    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # related field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        ImagePosts, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        '''
        order comments by most recent
        '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment from {self.user}"
