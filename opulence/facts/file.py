from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class File(BaseFact):
    _name_ = "File"
    _description_ = "Represent a file"
    _author_ = "Henry"
    _version_ = 1

    def setup(self):
        self.filename = StringField(mandatory=True)
        self.extension = StringField(mandatory=False)
        self.hash = StringField(mandatory=False)
        self.fullPath = StringField(mandatory=False)
        self.relativePath = StringField(mandatory=False)
