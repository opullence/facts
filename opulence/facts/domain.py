from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class Domain(BaseFact):
    _name_ = "Domain name"
    _description_ = "Represent a domain name"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.fqdn = StringField(mandatory=True)
        self.whois = StringField()
