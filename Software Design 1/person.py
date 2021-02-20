from address import Address


class Person:
    def __init__(self,first,last,dob,phone,address):
        self.first=first
        self.last=last
        self.Date_Of_Birth=dob
        self.phone=phone
        self.address=[]

        if (isinstance(address,Address)):
            self.address.append(address)
        elif  isinstance(address,list):
            for entry in address:
                if not isinstance(entry,Address):
                    raise Error("Invalid Address")
            self.address=address
        else:
            raise Error("Invalid Address")
    def add_address(self,address):
        if not isinstance(address,Address):
            raise Error("Invlid Adrress")
        self.address.append(address)

