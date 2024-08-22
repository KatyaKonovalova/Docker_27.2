import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_product(course):
    """Создает продукт в страйпе"""

    return stripe.Product.create(name=course.name)


def create_price(product, payment_sum):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        product=product.get('id'),
        currency='rub',
        unit_amount=int(payment_sum) * 100
    )


def create_session(price):
    """Создает сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url='https://127.0.0.1:8000/',
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment'
    )
    return session.get('id'), session.get('url')
