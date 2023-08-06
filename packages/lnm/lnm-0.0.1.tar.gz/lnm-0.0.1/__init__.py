import datetime
import requests
import base64
from requests.auth import HTTPBasicAuth

def generate_access_token():
    #consumer_key = keys.consumer_key
    #consumer_secret = keys.consumer_secret
    consumer_key = "18VioSM2JMDOlgwAGkrR5RK8qnSIf3kR"
    consumer_secret = "HrFh3b2eMYGuIAAW"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json()
    access_token = json_response['access_token']
    #access_token = "UPsg086oCEvPB0OGTqBqGPor8va2"
    return access_token

def lipa_na_mpesa(amount, phone, tracking_number):
    time = datetime.datetime.now()
    timestamp = time.strftime('%Y%m%d%H%M%S')
    #data = keys.business_shortcode + keys.lipa_na_mpesa_passkey + timestamp
    data = "174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + timestamp
    encoded_string = base64.b64encode(data.encode())
    password = encoded_string.decode('utf-8')
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }

    request = {
        "BusinessShortCode": "174379",
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        #"Amount": "1",
        "PartyA": phone,
        "PartyB": "174379",
        "PhoneNumber": phone,
        "CallBackURL": "https://postantsaapis.herokuapp.com/api/lnm_callback_url/",
        "AccountReference": tracking_number,
        "TransactionDesc": "Booking Payment"
    }
    response = requests.post(api_url, json = request, headers=headers)
    print(response.text)
    return response