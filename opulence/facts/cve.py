from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class CVE(BaseFact):
    _name_ = "CVE"
    _description_ = "Common vulnerabilities exposures identifier"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.id = StringField(mandatory=True, default="CVE-2019-9815")
        self.description = StringField()
