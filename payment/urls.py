# urls.py

from django.urls import path
from django.views.generic import TemplateView
from .views import PaymentView

urlpatterns = [
    path('', PaymentView.as_view(), name='payment'),
    path('success/', TemplateView.as_view(template_name='payment_success.html'), name='payment_success'),
]
