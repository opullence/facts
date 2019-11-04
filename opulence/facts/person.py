from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class Person(BaseFact):
    _name_ = "Person"
    _description_ = "Represent a person firstname and lastname"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.lastname = StringField(mandatory=True)
        self.firstname = StringField(mandatory=True)
