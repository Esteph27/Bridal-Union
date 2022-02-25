from django.forms import ModelForm
from .models import CustomerAccount
# from .models import Booking

class CustomerAccountForm(ModelForm):
    '''
    create customer account form
    '''
    class meta:
        model = CustomerAccount
        fields = [
            'user.first_name',
            'user.last_name',
            'user.email',
            'user.password',
            'contact_number',
            'wedding_date',
        ]


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
#             'price_range',
#         ]
