class Battery:

    def __init__(self, capacity: int, charge_level: int) -> None:
        if not capacity >= 0:
            raise ValueError("Invalid value for the capacity.")
        if not charge_level >= 0:
            raise ValueError("Invalid value for the charge_level.")
        self._capacity = capacity
        self._charge_level = charge_level
        
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def charge_level(self):
        return self._charge_level
    
    def use(self, hours):
        pass
    
    def recharge(self):
        pass