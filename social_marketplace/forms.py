from django.forms import ModelForm


class Bookingform(ModelForm):
    '''
    model for customer booking information
    '''

    # field variables
    bookingref = models.CharField(max_length=10, unique=True)
    date_of_booking = models.DateTimeField()
    
    #related fields
    customer_name_booking = models.ForeignKey(
       CustomerAccountInfo, on_delete=models.CASCADE, related_name="customer_booking"
    )
    designer_name_booking = models.ForeignKey(
       Designer, on_delete=models.CASCADE, related_name="customer_booking"
    )

    def __str__(self):
        return self.bookingref