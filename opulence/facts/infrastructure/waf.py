from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class Waf(BaseFact):
    _name_ = "Waf"
    _description_ = "Web application firewall."
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.name = StringField(mandatory=True, default="Cloudflare")
        self.vendor = StringField()
