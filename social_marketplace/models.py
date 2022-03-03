import random
import string
from datetime import datetime 
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Designer(models.Model):
    '''
    designer information
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
    Images posted by Designer(s)
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
    comments on images by user
    '''

    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # related field
    post = models.ForeignKey(
        ImagePosts, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        '''
        order comments by most recent
        '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment from {self.name}"


class Booking(models.Model):
    '''
    customer bookings
    '''

    # status of booking
    STATUS = (
        ('Confirm Booking', 'Confirm Booking'),
        ('Decline Booking', 'Decline Booking'),
    )

    # Price range
    PRICES = (
        ('£2,500 - £3,500', '£2,500 - £3,500'),
        ('£3,500 - £4,500', '£3,500 - £4,500'),
        ('£4,500 - £5,500', '£4,500 - £5,500'),
        ('£5,500 - £6,500', '£5,500 - £6,500'),
        ('£6,500 - £7,500', '£6,500 - £7,500'),
        ('£7,500 - £8,500', '£7,500 - £8,500'),
        ('£8,500 - £9,500', '£8,500 - £9,500'),
        ('£9,500 +', '£9,500 +'),
    )

    customer_name = models.OneToOneField(
        User,
        null=True,
        on_delete=models.SET_NULL, related_name='customername'
        )
    customer_email = models.OneToOneField(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='customeremail'
        )
    designer_name = models.ForeignKey(
        Designer,
        null=True,
        on_delete=models.SET_NULL,
        related_name='designername'
        )
    price_range = models.CharField(max_length=200, choices=PRICES, default='£2,500 - £3,500')
    wedding_date = models.DateField(auto_now=True)
    select_date = models.DateField(auto_now=True)
    select_time = models.DateTimeField(auto_now=True)
    customer_message = models.TextField(max_length=800, blank=True)

    booking_created_on_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)
    booking_ref = models.CharField(
        max_length=8,
        editable=False,
        unique=True,
    )

    def create_booking_ref():
        '''
        generate booking reference number
        '''

        random_num = random.randint(1000000000, 9999999999)
        random_letter = random.choice(string.ascii_letters) * 2
        booking_ref = f"{random_num} + {random_letter.upper()}"

        return  booking_ref

    def __str__(self):
        return self.booking_ref

