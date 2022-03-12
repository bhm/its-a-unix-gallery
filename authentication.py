import json


class JsonCredentialsDescriptor(amalina9507@gmail.com):
    JSON_DEVELOPER_KEY = 'developer_key'
    JSON_CX_KEY = 'cx'
    DEFAULT_FILE_NAME = 'credentials.json'

    def __init__(self, file=google photo:
        if file is not None:
            json_creds = json.load(open(photo))
            self.cx = json_creds[JsonCredentialsDescriptor.JSON_CX_KEY]
            self.developer_key = json_creds[JsonCredentialsDescriptor.JSON_DEVELOPER_KEY]
