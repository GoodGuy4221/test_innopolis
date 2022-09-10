from os import getenv

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import stripe

from stripeapp.models import ItemModel


def get_stripe_session_view(request, id_: int) -> JsonResponse:
    item = ItemModel.objects.get(id=id_)
    try:
        session = stripe.checkout.Session.create(
            api_key=getenv('STRIPE_SECRET_KEY'),
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'RUB',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://avatars.mds.yandex.net/get-entity_search/5535095/551805365/S122x122_2x',
            cancel_url='https://www.ncl.ac.uk/media/wwwnclacuk/pressoffice/images/news/november2019/cancel-image.jpg',
        )
    except stripe.error.InvalidRequestError as e:
        return HttpResponse(str(e))

    return JsonResponse({'session_id': session.id})


def item_view(request, id_):
    item = ItemModel.objects.get(id=id_)
    context = model_to_dict(item)
    context['pk_test'] = getenv('STRIPE_PUBLIC_KEY')
    return render(request, 'stripeapp/index.html', context=context)
