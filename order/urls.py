from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    # path('order/notification/', views.notifications, name='notification')
]
