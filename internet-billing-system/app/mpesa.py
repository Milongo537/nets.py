from flask import Blueprint, request, jsonify
import requests

mpesa_bp = Blueprint('mpesa', __name__)

# M-Pesa API credentials and URLs
MPESA_BASE_URL = 'https://sandbox.safaricom.co.ke'
LIPA_NA_MPESA_URL = f'{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest'
SHORTCODE = 'your_shortcode'
LIPA_NA_MPESA_SHORTCODE = 'your_shortcode'
LIPA_NA_MPESA_PASSKEY = 'your_passkey'
LIPA_NA_MPESA_LIVE_SHORTCODE = 'your_live_shortcode'
LIPA_NA_MPESA_LIVE_PASSKEY = 'your_live_passkey'
LIPA_NA_MPESA_LIVE_URL = f'{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest'

def generate_token():
    api_url = f"{MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_url, auth=(SHORTCODE, LIPA_NA_MPESA_PASSKEY))
    json_response = response.json()
    return json_response['access_token']

@mpesa_bp.route('/pay', methods=['POST'])
def pay():
    phone_number = request.json.get('phone_number')
    amount = request.json.get('amount')
    token = generate_token()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "BusinessShortCode": LIPA_NA_MPESA_SHORTCODE,
        "Password": LIPA_NA_MPESA_PASSKEY,
        "Timestamp": "your_timestamp",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": LIPA_NA_MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://your_callback_url",
        "AccountReference": "AccountReference",
        "TransactionDesc": "Payment for internet service"
    }

    response = requests.post(LIPA_NA_MPESA_URL, json=payload, headers=headers)
    return jsonify(response.json())

@mpesa_bp.route('/callback', methods=['POST'])
def callback():
    # Handle M-Pesa callback here
    return jsonify({"status": "success"})