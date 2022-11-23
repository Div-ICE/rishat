import stripe
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from rishat.settings import (DOMAIN_URL, STRIPE_PUBLIC_KEY,
                                    STRIPE_SECRET_KEY)

from .models import Item


def get_item_page(request, id):
    if request.method == "GET":
        item = get_object_or_404(Item, id=id)
        return render(request,
                      template_name='item.html',
                      context={
                          "id": id,
                          "name": item.name,
                          "description": item.description,
                          "price": item.price/100,
                          "stripe_public_key": STRIPE_PUBLIC_KEY,
                      })


stripe.api_key = STRIPE_SECRET_KEY


def buy_item(request, id):
    if request.method == "GET":
        item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=DOMAIN_URL + 'success/',
            cancel_url=DOMAIN_URL + 'item/' + str(id),
        )
        return HttpResponse(
                json.dumps(session),
                content_type='application/json'
                )


class SuccessView(TemplateView):
    template_name = 'success.html'
