import os

creds = os.environ.get("AUTH_CREDS")
if creds:
    basic_auth = creds.split(",")
else:
    basic_auth = []
