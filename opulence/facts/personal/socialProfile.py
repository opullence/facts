from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class SocialProfile(BaseFact):
    _name_ = "Social network profile"
    _description_ = "Represent a social network profile for a given username"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.username = StringField(mandatory=True, default="johnsnow")
        self.site = StringField(mandatory=True, default="spotify")
        self.url = StringField(default="http://example.com")
