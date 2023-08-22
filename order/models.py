from django.db import models


# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    order_date = models.DateTimeField(auto_now_add=True)
    SUCCESS = 'success'
    FAILURE = 'failure'
    ORDER_STATUS_CHOICES = (
        (SUCCESS, 'Success'),
        (FAILURE, 'Failure'),
    )
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default=SUCCESS)

    def __str__(self):
        return '{}'.format(self.full_name)
