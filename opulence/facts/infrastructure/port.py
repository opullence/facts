from opulence.common.facts import BaseFact
from opulence.common.fields import StringField, IntegerField


class Port(BaseFact):
    _name_ = "Port"
    _description_ = "Represent an UDP or TCP network port and state"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.number = IntegerField(mandatory=True, default=80)
        self.state = StringField()
        self.transport = StringField()
