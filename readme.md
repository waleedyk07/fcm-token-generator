# fcm-token-generator
## Install Dependancies
`pip install -r requirements.txt`
## JSON Key
Generate JSON key file for google service account and place inside src directory.
## Generate Token
* Update the key filename (`myjazz-b2c-6c79cec24e95.json`) in below line inside `main.py` file.<br />
`credentials = service_account.Credentials.from_service_account_file('myjazz-b2c-6c79cec24e95.json', scopes=SCOPES)`
* Generate token using below command inside src directory.<br />
`python main.py`
