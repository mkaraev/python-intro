import json


class BaseFormat:
    def format(self, patients):
        raise NotImplementedError

    @staticmethod
    def from_format(format):
        if format == "plain":
            return PlainFormat()
        if format == "json":
            return JsonFormat()


class PlainFormat(BaseFormat):
    def format(self, patients):
        return "\n".join([str(patient) for patient in patients])


class JsonFormat(BaseFormat):
    def format(self, patients):
        data = [patient.__dict__ for patient in patients]
        return json.dumps(data, indent=4, sort_keys=True)
