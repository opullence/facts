from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class File(BaseFact):
    _name_ = "File"
    _description_ = "Represent a file"
    _author_ = "Henry"
    _version_ = 1

    def setup(self):
        self.filename = StringField(mandatory=True)
        self.url = StringField()
        self.extension = StringField()
        self.hash = StringField()
        self.fullPath = StringField()
        self.relativePath = StringField()
