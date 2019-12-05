from opulence.common.facts import BaseFact
from opulence.common.fields import IntegerField, StringField


class VulDB(BaseFact):
    _name_ = "VulDB"
    _description_ = "VULDB vulnerability identifier"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.id = IntegerField(mandatory=True, default=133852)
        self.description = StringField()
