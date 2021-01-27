class Person:

    def __init__(self, name: str, address: str,
                 phone: str, identification: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.id = identification

    def __eq__(self, other):
        return self.name == other.name and self.address == other.address and \
                self.phone == other.phone and self.id == other.id
