class RawPart:
    def __init__(self, plastic, propellant, status_high=False, status_ground=False):
        self._plastic = plastic
        self._propellant = propellant
        self.status_high = status_high
        self.status_ground = status_ground

    @property
    def plastic(self):
        return self._plastic
    
    @property
    def propellant(self):
        return self._propellant
    
    @plastic.setter
    def plastic(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be a Strng')
        self._plastic = value

    @propellant.setter
    def propellant(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be a String')
        self._propellant = value

    def set_location():
        pass

class PaintedPart(RawPart):
    pass

class PurchasingPart:
    pass

class ProductionPart:
    pass

class StorageLocation:
    pass
