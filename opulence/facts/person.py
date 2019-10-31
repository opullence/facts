from opulence.common.bases.baseFact import BaseFact
from opulence.common.fields import StringField


class Person(BaseFact):
    _name_ = "Person"
    _description_ = "Represent a person firstname and lastname"
    _author_ = "Louis Jurczyk"
    _version_ = 1

    def setup(self):
        self.sdf = StringField(mandatory=False)
        self.lastname = StringField(default="John")
        self.firstname = StringField(default="Snow")
