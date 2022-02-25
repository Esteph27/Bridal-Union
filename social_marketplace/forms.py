from django.forms import ModelForm
from .models import CustomerAccount
# from .models import Booking

class CustomerAccountForm(ModelForm):
    '''
    create customer account form
    '''
    class meta:
        model = CustomerAccount
        fields = '__all__'


# class BookingForm(ModelForm):
#     '''
#     booking form
#     '''
#     class Meta:
#         model = Booking
#         fields = [
#             'customer_name',
#             'customer_email',
#             'designer_name',
            #'date of wedding'
#             'price_range',
#         ]
