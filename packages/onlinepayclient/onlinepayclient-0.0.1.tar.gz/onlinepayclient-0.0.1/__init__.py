import base64
import datetime

import requests
from requests.auth import HTTPBasicAuth


class LNMOnlineClient(object):
    def __init__(self, data=None):
        try:
            self.consumer_key = data['consumer_key'] or None
            self.consumer_secret = data['consumer_secret'] or None
            self.business_shortcode = data['business_shortcode'] or None
            self.lipa_na_mpesa_passkey = data['lipa_na_mpesa_passkey'] or None
            self.callback_url = data['callback_url']
        except KeyError:
            return {"Error": "Please Fill in data correctly"}

    def test_generate_access_token(self):
        consumer_key = self.consumer_key
        consumer_secret = self.consumer_secret
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        json_response = r.json()
        access_token = json_response['access_token']
        return access_token
    
    def test_initiate_lnm_online_stk(self, data):
        time = datetime.datetime.now()
        timestamp = time.strftime('%Y%m%d%H%M%S')
        pass_data = self.business_shortcode + self.lipa_na_mpesa_passkey + timestamp
        encoded_string = base64.b64encode(pass_data.encode())
        password = encoded_string.decode('utf-8')
        access_token = self.test_generate_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }

        try:
            amount = data['amount']
            phone = data['phone']
            account_ref=data['account_ref']
            description=data['description']

            request = {
                "BusinessShortCode": self.business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone,
                "PartyB": self.business_shortcode,
                "PhoneNumber": phone,
                "CallBackURL": self.callback_url,
                "AccountReference": account_ref,
                "TransactionDesc": description,
            }
            response = requests.post(api_url, json = request, headers=headers)
            json_res = response.json()
            return json_res
        except KeyError:
            return {"Error": "Enter Valid data"}


    