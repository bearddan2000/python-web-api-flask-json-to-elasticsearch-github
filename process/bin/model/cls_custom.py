from json import JSONEncoder

# subclass JSONEncoder
class CustomJSONEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__