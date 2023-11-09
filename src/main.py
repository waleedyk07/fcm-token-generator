import google.auth.transport.requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
credentials = service_account.Credentials.from_service_account_file('myjazz-b2c-6c79cec24e95.json', scopes=SCOPES)
request = google.auth.transport.requests.Request()
credentials.refresh(request)
# print(credentials.__dict__)
print(credentials.token)