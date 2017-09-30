import json


class JsonCredentialsDescriptor(object):
    JSON_DEVELOPER_KEY = 'developer_key'
    JSON_CX_KEY = 'cx'
    DEFAULT_FILE_NAME = 'credentials.json'

    def __init__(self, file=DEFAULT_FILE_NAME):
        if file is not None:
            json_creds = json.load(open(file))
            self.cx = json_creds[JsonCredentialsDescriptor.JSON_CX_KEY]
            self.developer_key = json_creds[JsonCredentialsDescriptor.JSON_DEVELOPER_KEY]
