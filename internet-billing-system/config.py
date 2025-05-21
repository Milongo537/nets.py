import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # M-Pesa configuration
    MPESA_CONSUMER_KEY = os.environ.get('MPESA_CONSUMER_KEY') or 'your_consumer_key_here'
    MPESA_SECRET_KEY = os.environ.get('MPESA_SECRET_KEY') or 'your_secret_key_here'
    MPESA_SHORTCODE = os.environ.get('MPESA_SHORTCODE') or 'your_shortcode_here'
    MPESA_LIVE_URL = 'https://api.safaricom.co.ke'
    MPESA_SANDBOX_URL = 'https://sandbox.safaricom.co.ke'