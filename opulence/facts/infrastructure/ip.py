from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class IPv4(BaseFact):
    _name_ = "IPv4"
    _description_ = "Represent an IP address version 4"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.address = StringField(mandatory=True, default="127.0.0.1")

    def get_summary(self):
        return "{}".format(self.address.value)


class IPv6(BaseFact):
    _name_ = "IPv6"
    _description_ = "Represent an IP address version 6"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.address = StringField(mandatory=True, default="127.0.0.1")

    def get_summary(self):
        return "{}".format(self.address.value)
