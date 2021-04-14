from pyexpat.errors import messages
from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from accounts.models import Account
from rest_framework.decorators import api_view
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["POST", ])
def create_payment(request):
    account_id = request.data.get("account_id")

    try:
        user_account = Account.objects.get(pk=account_id)

        if user_account.stripe_customer_id != '' and user_account.stripe_customer_id is not None:
            customer = stripe.Customer.retrieve(
            user_account.stripe_customer_id)

        else:
            customer = stripe.Customer.create(
                email=user_account.username,
            )
            user_account.stripe_customer_id = customer['id']
            user_account.one_click_purchasing = True
            user_account.save()

        data = request.data
        intent = stripe.PaymentIntent.create(
            amount=(data.get("amount", None))*100,
            currency='usd',
            setup_future_usage='off_session',
            customer=user_account.stripe_customer_id
        )

        # stripe.Subscription.create(
        #     customer='{{CUSTOMER_ID}}',
        #     items=[
        #         {
        #             'price': '{{STANDARD_MONTHLY_USD_PRICE_ID}}',
        #             'quantity': 2,
        #         },
        #     ]
        # )

        return Response({
          'clientSecret': intent['client_secret']
        }, status=HTTP_200_OK)

    except stripe.error.CardError as e:
        body = e.json_body
        err = body.get('error', {})
        return Response({"message": f"{err.get('message')}"}, status=HTTP_400_BAD_REQUEST)

    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        messages.warning(self.request, "Rate limit error")
        return Response({"message": "Rate limit error"}, status=HTTP_400_BAD_REQUEST)

    except stripe.error.InvalidRequestError as e:
        print(e)
        # Invalid parameters were supplied to Stripe's API
        return Response({"message": "Invalid parameters"}, status=HTTP_400_BAD_REQUEST)

    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        return Response({"message": "Not authenticated"}, status=HTTP_400_BAD_REQUEST)

    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        return Response({"message": "Network error"}, status=HTTP_400_BAD_REQUEST)

    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        return Response({"message": "Something went wrong. You were not charged. Please try again."}, status=HTTP_400_BAD_REQUEST)

    except Exception as e:
        # send an email to ourselves
        return Response({"message": "A serious error occurred. We have been notifed."}, status=HTTP_400_BAD_REQUEST)

    return Response({"message": "Invalid data received"}, status=HTTP_400_BAD_REQUEST)
