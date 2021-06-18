import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from django.contrib import messages

serviceAccountKey = {
  "type": "service_account",
  "project_id": "ard-app-d98e6",
  "private_key_id": "acd6f6e850b60a997f93e068b4955d01c07ede75",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPlzdijzWP/gfr\n25Ud5hzkck4SrArbAWbGVpOoDBp6bkd6ntj5e04ppCRQ7DW5pSvkqphTLgWH4Y0c\nXT/DBTKsZIZBBBzSJRJzRD1cRIKzC20huUo+xV/gm8Fc6sjCpo5c3Mw2iFqJtkqA\ntPuR7TwwpgjZLJ++7XcRkeLEmnNuk6ZNrQzImaenanZ6Sqc7pjThrFLInADN2e9y\nnSGA5UorGWcnAKbF8zZAtdHBs/u/xMLN+7eQpSfjTi5KaY66wXvi3CEcOjdvyzdR\nF33ScgVFO59fDOJF9TXTf5ayiobL0gOmQQgclI3tw1KZ1X5BexkTYGf/9dc4w0Ke\n/ODcNwYtAgMBAAECggEALsBQBV7aQcEEuK39sbuawyopAhSD51mz8zQZUe3T4sHG\nUEvI8rq92ivwz9a6rMIRlhCDeKwzK6x00q//haS8ik2jXK4X7Y3Sz2nNZeO6Caen\nnsIzgdqCoruBOzNXHltTUX+acCeaOEx5D+5yf6VNemlSMdLWcTHasHbJ+twL5hlr\nlczwhJdA9gNCR3tYKHOKkR4RrlDFuXxrjIIMYJKzah0koIoLi2g6HXnpxYcl8les\n2wfUD31lJI1IpKavChIce0ivYfx3EswFie0Nxgf+fkNq5tmI6C/B6FQdq7VmAZx5\nwXe3cj/ZpLb/fQPnlEiohpSstW56XgGqWVReTydvkwKBgQDxpmZoMLFRyQV+9gEn\nE2Pxm1DEU8AVfGRNdAvwhlEIe/vKand91bZSggbc3L/Kv459a/DZAQDP7OtqMy4J\nJDFuBySNXOtUXcsiFcmQ/9uxMqJN9CoPoy+SUSPePZHLyiKxXxnkYTady8DNfLmu\nrmo6d4nVk83+FtRTetcZTaqLYwKBgQDb6wqf4j4UDt6Djd4x4A7M8jUJiXK2wBuf\nHc2qc2SIXf5EHnGoBAGULlBWLqCL9zDLmhJPBxZiE0rIkRvE2UbXSyDW8Bw7B5vy\nIHP+Tf2U0yl3rOjzIJ002SAC3nYTzYv712ADuQUvzelME0I4G6tLFCfB/RgKuuwX\nlKIc75+FLwKBgQCpA+ewjA4Z0+4CJPIdcJSA0k8lYiaBYKWO/tGzA179/inYI6s7\n2hRRlRxTshp7Jov08WBdhzQYOe9WMkHKpwPjnx9TuF/ofEmtp2t5/Vqdj3qx50rb\n8Rk+z3203X9x+AlX4dpsQApBR9esYcZFhTxLdHx1Y5G6XCFZ2htEWWwlXQKBgCHN\nIYfrhTEeC/NaZdFyp7O2cpJxrtEJ+/Tb5tWRAN243LDpoPx7CScWa0Cj0AdTSgux\nNakx5K3UW0UykHsUDkBfCsAejahBBiYT+OAYaqZqQlBjojZkR+VsjfAC81Ed4asm\nslpAINz1ICuSNjZbglt60JWPaheUHV+Od9BMwE7/AoGANGf+Hmvfji3D10R2buQZ\no9QGumR6umE9Y6J4KCGntIwmMbTtSGD+kiHnKRso2xkLOthbiG8Dq7DGP7bpLnWy\nm3uMPM9D7nqwos5AlSSxVH3YKGMAHa4NhJ/+vsUrrYTM84zDtE/7OahLUhwIKH8+\nEujYPY+rh3djOkOKIFsNK+g=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-7ao09@ard-app-d98e6.iam.gserviceaccount.com",
  "client_id": "103537905902219767285",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7ao09%40ard-app-d98e6.iam.gserviceaccount.com"
}

# Setup
cred = credentials.Certificate(serviceAccountKey)
firebase_admin.initialize_app(cred)
db = firestore.client()