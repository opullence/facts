from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class OperatingSystem(BaseFact):
    _name_ = "OperatingSystem"
    _description_ = "Represent an operating system name, version and vendor "
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.address = StringField(mandatory=True, default="127.0.0.1")