import os
""" aws access info """
DOMAIN = 'https://www.job-assist'
AWS_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxx'
AWS_SECRET_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxx'
BUCKET_NAME_PRODUCT = 'xxxxxxxxxxxxxxxxxx'
BUCKET_NAME_DEV = 'xxxxxxxxxxxxxxxxxx'
SMS_APPLICATION_ID = "xxxxxxxxxxxxxxxxxx"
SMS_ORIGINATION_NUMBER = '+xxxxxxxxxxxxxxxxxx'

if os.getenv('APP', '') == 'themotherlode':
    BUCKET_NAME = 'attachment-product'
    AWS_BASE_URL = 'xxxxxxxxxxxxxxxxxx'
    AWS_BASE_DOCUMENT_URL = 'xxxxxxxxxxxxxxxxxx'
    AWS_AVATAR_URL = 'xxxxxxxxxxxxxxxxxx'
else:
    BUCKET_NAME = 'xxxxxxxxxxxxxxxxxx'
    AWS_BASE_URL = 'xxxxxxxxxxxxxxxxxx'
    AWS_BASE_DOCUMENT_URL = 'xxxxxxxxxxxxxxxxxx'
    AWS_AVATAR_URL = 'xxxxxxxxxxxxxxxxxx'


""" mailgun api key"""
MAIL_GUN_API_KEY = 'xxxxxxxxxxxxxxxxxx'


""" braintree keys"""
BRAINTREE_MERCHANT_ID = '9dwqvgqgnwpz5tc8'
BRAINTREE_PUBLIC_KEY = 'f7jbsr9v7b3x2wcj'
BRAINTREE_PRIVATE_KEY = '5ce2b09f4071a8f6eb17e5fc63f93a98'


""" stripe key"""
# STRIPE_API_KEY = 'xxxxxxxxxxxxxxxxxx'
# STRIPE_API_KEY = 'xxxxxxxxxxxxxxxxxx'
#
if os.getenv('APP', '') == 'themotherlode':
    STRIPE_API_KEY = 'xxxxxxxxxxxxxxxxxx'
else:
    STRIPE_API_KEY = 'xxxxxxxxxxxxxxxxxx'


""" notification types """
NOTIFICATION_TRANSFER = 0
NOTIFICATION_UPDATE = 1
NOTIFICATION_ALARM = 2

""" notification states """
UNCHECKED_NOTIFICATION = 0
CHECKED_NOTIFICATION = 1

""" transfer states """
TRANSFER_PENDING = 0
TRANSFER_RETURN_REQUEST = 1
TRANSFER_REJECTED = 2
TRANSFER_ACCEPTED = 3
TRANSFER_INSERTED = 4
TRANSFER_REMOVED = 5

""" transaction states """
RETURN_REQUESTED = -1
RETURN_STARTED = 0
RETURN_IN_PROGRESS = 1
RETURN_COMPLETED = 2
COMPLETED = 3


""" attachment type """
TMP_ATTACHMENT = 0
ARTIFACT = 1
DOCUMENT = 2
AVATAR = 3

""" user role """
ROLE_ADMIN = 0
ROLE_USER = 1
ROLE_GROUP_OWNER = 2


NOTIFICATION_FILE_COMPLAINT = 11
NOTIFICATION_LEAVE_COMPLAINT = 11
NOTIFICATION_SOLVE_COMPLAINT = 11


PAYPAL_CLIENT_ID = 'AcwMcCFNq5eq6q-KfYYGSjri_tdXc_79ZrPikQ8aT9fOTJExNmR5jP74hgHsE8Kgex0fRhdLMVdFRaJg'
PAYPAL_SECURITY = 'EAD09Xf-l5Hcm6AsivINwZ-LiBViIQAfLCgktatPfbOn02sPu5PWPWA5-M2o0h_52DaeKaZw4HTFf471'
MERCHANT_ID = 'ID3WH5FGBXEAD9U'


STRIPE_AVAILABLE_COUNTRIES = ['AU', 'AT', 'BE', 'CA', 'DK', 'FI', 'FR', 'DE', 'CH', 'HK', 'IE', 'IT', 'JP', 'LU', 'NL',
                              'NZ', 'NO', 'PT', 'SG', 'ES', 'SE', 'GB', 'US']

SHIP_ENGINE_APP_KEY = 'rWKkoR+0AHBOqRUafRahmfUO0EgcEjwd6Et8XeC1hsg'

PROMO_HASHID_SALT = "xxxxxxxxxxxxxxxxxx"
COA_HASHID_SALT = "xxxxxxxxxxxxxxxxxx"
CONFIRM_CODE_HASHID_SALT = "xxxxxxxxxxxxxxxxxx"

# Frontend router
FRONTEND_ROUTER_MANAGEMENT = "/manage/transaction"
FRONTEND_ROUTER_EXPERT = "/manage/authentication/expert"
FRONTEND_ROUTER_AUTH = "/manage/authentication"
