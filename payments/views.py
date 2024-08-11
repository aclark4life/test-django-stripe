# views.py

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from .forms import PaymentsForm
from .models import Payment

class PaymentsView(View):
    def get(self, request):
        # Set the amount you want to charge
        amount = 50.00  # for example, 0.00
        form = PaymentsForm(initial={'amount': amount})
        return render(request, 'payments.html', {'form': form, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

    def post(self, request):
        form = PaymentsForm(request.POST)
        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY
            token = form.cleaned_data['stripeToken']
            amount = int(form.cleaned_data['amount'] * 100)  # Stripe uses cents

            try:
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    description='Example charge',
                    source=token,
                )

                # Save the payments in the database
                payments = Payments.objects.create(
                    amount=form.cleaned_data['amount'],
                    stripe_charge_id=charge.id
                )

                return redirect('payments_success')  # Redirect to a success page

            except stripe.error.StripeError as e:
                # Handle error
                return render(request, 'payments.html', {'form': form, 'error': str(e), 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

        return render(request, 'payments.html', {'form': form, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})
