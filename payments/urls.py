# urls.py

from django.urls import path
from django.views.generic import TemplateView
from .views import PaymentsView

urlpatterns = [
    path('', PaymentsView.as_view(), name='payments'),
    path('success/', TemplateView.as_view(template_name='payments_success.html'), name='payments_success'),
]
