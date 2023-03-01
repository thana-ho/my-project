class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Admin(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

class Customer(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

class FrontDeskOfficer:
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)