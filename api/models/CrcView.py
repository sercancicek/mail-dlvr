import json


class CrcView:
    email: str
    full_name: str
    has_mail_sent: bool
    has_receiver_clicked: bool
    duration: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
