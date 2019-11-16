from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class Username(BaseFact):
    _name_ = "Username"
    _description_ = "Represent an online username"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.name = StringField(mandatory=True)
