import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from django.contrib import messages

# service key needed #

# Setup
cred = credentials.Certificate(serviceAccountKey)
firebase_admin.initialize_app(cred)
db = firestore.client()
