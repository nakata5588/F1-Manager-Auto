class Driver:
    def __init__(self, name: str, number: int, nationality: str):
        self.name = name
        self.number = number
        self.nationality = nationality

    def __repr__(self):
        return f"Driver(name={self.name}, number={self.number}, nationality={self.nationality})"