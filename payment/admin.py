# admin.py

from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'stripe_charge_id', 'timestamp')
    search_fields = ('stripe_charge_id',)
    list_filter = ('timestamp',)

    # readonly_fields = ('amount', 'stripe_charge_id', 'timestamp')

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
