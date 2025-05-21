import requests

# Dummy MPESA integration for demonstration purposes.
# In production, use official Safaricom Daraja API and secure credentials.

MPESA_API_URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
MPESA_CONSUMER_KEY = "your_consumer_key"
MPESA_CONSUMER_SECRET = "your_consumer_secret"
MPESA_SHORTCODE = "174379"
MPESA_PASSKEY = "your_passkey"
CALLBACK_URL = "https://yourdomain.com/mpesa/callback"

def initiate_payment(phone_number, amount, account_reference, transaction_desc):
    # This is a placeholder. In production, implement OAuth, password generation, and full API logic.
    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": "GENERATED_PASSWORD",
        "Timestamp": "TIMESTAMP",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": CALLBACK_URL,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }
    # Simulate a successful payment response
    return {
        "ResponseCode": "0",
        "ResponseDescription": "Success. Request accepted for processing",
        "MerchantRequestID": "12345",
        "CheckoutRequestID": "67890"
    }

# Example usage:
# response = initiate_payment("254712345678", 20, "hourly_3mbps", "Internet Plan Payment")
# print(response)