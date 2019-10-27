from . import BaseFact, Field


class Person(BaseFact):
    _name_ = "Person"
    _description_ = "Represent a person firstname and lastname"
    _author_ = "Louis Jurczyk"
    _version_ = 1

    def setup(self):
        self.sdf = Field(mandatory=False)
        self.lastname = Field()
        self.firstname = Field()
