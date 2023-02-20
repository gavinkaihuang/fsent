import json
from fsent.models import User

class UserJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'id': obj.id,
                'username': obj.username,
                'email': obj.email,
                # add any other attributes you want to include in the serialized object
            }
        return super().default(obj)