class Operator:

    def __init__(self, name: str) -> None:
        if not self.validate_name(name):
            raise ValueError("Invalid name. Name must be a non-empty string.")
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @staticmethod
    def validate_name(name):
        """Validates that the name is a non-empty string."""
        return isinstance(name, str) and bool(name.strip())