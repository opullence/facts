from opulence.common.facts import BaseFact
from opulence.common.fields import StringField


class GitRepository(BaseFact):
    _name_ = "File"
    _description_ = "Remote git repository (github, gitlab, bitbucket ..)"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.url = StringField(
            mandatory=True, default="https://github.com/jurelou/opulence.git"
        )
        self.host = StringField()
        self.username = StringField()
        self.project = StringField()

    def get_summary(self):
        return "{}".format(self.url.value)
