from opulence.common.fields import StringField
from opulence.facts import BaseFact


class Person(BaseFact):
    _name_ = "Person"
    _description_ = "Represent a person firstname and lastname"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.sdf = StringField(mandatory=False)
        self.lastname = StringField()
        self.firstname = StringField()
