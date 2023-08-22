from django.contrib import messages
from django.utils import timezone
from .models import Order
from django.shortcuts import render, redirect


# Create your views here.

def checkout(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')

        # Create an Order instance with the gathered data
        order = Order.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            zip_code=zip_code,
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
            order_status=Order.SUCCESS,
            order_date=timezone.now()  # Use timezone to get the current time
        )
        messages.success(request, 'Order placed successfully!')

    return render(request, 'checkout.html')
