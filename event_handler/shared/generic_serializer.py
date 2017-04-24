import json


class GenericEncoder(json.JSONEncoder):
    encoding_info = {}

    def default(self, o):
        try:
            dicted = {}
            for key, t_key in self.encoding_info.items():
                dicted[key] = t_key(getattr(o, key, None))
            return dicted
        except:
            return json.JSONEncoder.default(self, o)
