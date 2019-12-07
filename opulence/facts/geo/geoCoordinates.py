from opulence.common.facts import BaseFact
from opulence.common.fields import IntegerField


class GeoCoordinates(BaseFact):
    _name_ = "GeoCoordinates"
    _description_ = "GPS coordinates (latitude / longitude)"
    _author_ = "Louis"
    _version_ = 1

    def setup(self):
        self.latitude = IntegerField(mandatory=True, default=42)
        self.longitude = IntegerField(mandatory=True, default=42)
