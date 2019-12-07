from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class Email(BaseFact):
    _name_ = "Email"
    _description_ = "Represent an email address"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.address = StringField(mandatory=True, default="john@example.com")
