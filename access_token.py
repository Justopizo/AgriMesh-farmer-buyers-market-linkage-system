import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'D6UVFW0NqI4Sir9HdLMeJIlGy0yX6YVXi76348J2yfnnlkev' 
    consumer_secret = 'qmhTOxyzaJfxYtlt0y2bZm7uORobP46TNG8t24KpNCxOAL6TnGdh65DAQPZYD4IL' 
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = r.json()
    formated_res = json.dumps(mpesa_access_token, indent=4)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    print(formated_res)
    


class LipanaMpesaPpassword:
    phoneno=254793031269
    amount=1
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
    
request = {
    "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
    "Password": LipanaMpesaPpassword.decode_password,
    "Timestamp": LipanaMpesaPpassword.lipa_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": LipanaMpesaPpassword.amount,
    "PartyA": 254793031269,
    "PartyB": LipanaMpesaPpassword.Business_short_code,
    "PhoneNumber": LipanaMpesaPpassword.phoneno,
    "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
    "AccountReference": "Justo Pizo",
    "TransactionDesc": "Testing stk push"
}
