class ClientData:

    def __init__(self, firstName, lastName, PhoneWorkCell, PhoneHome, address, city, state, zip):
        self.firstName = firstName
        self.lastName = lastName
        self.PhoneWorkCell = PhoneWorkCell
        self.PhoneHome = PhoneHome
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def print_client_Info(self):
        print(self.firstName,self.lastName, self.phoneWorkCell, self.phoneHome,self.address,
              self.city, self.state,self.zip)

    # getter method
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName
    
    def get_PhoneWorkCell(self):
        return self.PhoneWorkCell
    
    def get_PhoneHome(self):
        return self.PhoneHome
    
    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    # setter method
    def set_firstName(self, x):
        self.firstName = x

    def set_lastName(self, x):
        self.lastName = x

    def set_PhoneWorkCell(self, x):
        self.PhoneWorkCell = x

    def set_PhoneHome(self, x):
        self.PhoneHome = x

    def set_address(self, x):
        self.address = x

    def set_city(self, x):
        self.city = x

    def set_state(self, x):
        self.state = x

    def set_zip(self, x):
        self.zip = x