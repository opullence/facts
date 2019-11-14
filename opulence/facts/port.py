from opulence.common.facts import BaseFact
from opulence.common.fields import IntegerField, StringField


class Port(BaseFact):
    _name_ = "Port"
    _description_ = "Represent an UDP or TCP network port and state"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.number = IntegerField(mandatory=True)
        self.state = StringField()
        self.proto = StringField()
