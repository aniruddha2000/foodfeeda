from urllib import response
from django.shortcuts import render
import json
import os
import razorpay
from rest_framework.decorators import api_view
from rest_framework.response import Response
from donations.models import Donner_paydetails
from .serializers import OrderSerializer

@api_view(['POST'])
def start_payment(request):
    # request.data is coming from frontend
    amount = request.data['amount']
    name = request.data['name']

    # setup razorpay client
    client = razorpay.Client(auth=(os.getenv('PUBLIC_KEY'), os.getenv('SECRET_KEY')))


    # create razorpay order
    payment = client.order.create({"amount": int(amount) * 100,
                                   "currency": "INR",
                                   "payment_capture": "1"})

    # we are saving an order with isPaid=False
    order= Donner_paydetails.objects.create(
                                 ngo_name=name,
                                 amount=amount,
                                 order_payment_id=payment['id'])

    serializer = OrderSerializer(order)

    """order response will be 
     {
        "id": 4,
        "order_date": "03 February 2022 08:06 AM",
        "ngo_name": "test",
        "amount": "9",
        "order_payment_id": "order_IrSr3HB908pqqA",
        "rez_payment_id": "",
        "isPaid": false
    }"""

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)


@api_view(['POST'])
def handle_payment_success(request):
    # request.data is coming from frontend
    res = json.loads(request.data["response"])

    """res will be:
    {'razorpay_payment_id': 'pay_G3NivGft5Lx7I9e', 
    'razorpay_order_id': 'order_G3NhGHF655UfjQ', 
    'razorpay_signature': '76b2accbefde6cd2392b5njn7sj8ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
    """

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    # get order by payment_id which we've created earlier with isPaid=False
    order = Donner_paydetails.objects.get(order_payment_id=ord_id)

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=('rzp_test_9PhapTgkfwHU4D','F1azGBP3p8PYHoF10SisZ5N2'))

    # checking if the transaction is valid or not if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)

    if check is not None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order.rez_payment_id=response["razorpay_payment_id"]
    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)
