from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class Country(BaseFact):
    _name_ = "Country"
    _description_ = "Defines a country name and short code"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.name = StringField(mandatory=True, default="China")
        self.short_name = StringField()
        self.timezone = StringField()
