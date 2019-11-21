import uuid


class CustomTools:
    def __init__(self):
        pass

    def make_token(self):
        token = uuid.uuid4().hex
        return token
