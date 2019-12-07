from opulence.common.facts import BaseFact
from opulence.common.fields import StringField, IntegerField


class Banner(BaseFact):
    _name_ = "Banner"
    _description_ = r"""
        Banners are usually text messages displayed by a service.
        Banners usually contain information about a service, such as the version number.
        """
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.message = StringField(mandatory=True, default="Hello world")
        self.port = IntegerField()
        self.product = StringField()
