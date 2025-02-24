import json
import requests
from access_token import request, MpesaAccessToken

def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    response = requests.post(api_url, json=request, headers=headers)
    print(json.dumps(response.json(), indent= 4))

lipa_na_mpesa_online(request)