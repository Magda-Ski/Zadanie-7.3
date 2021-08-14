#from faker import Faker
#fake = Faker()



class BaseContacts:
    def __init__(self,name,surname,adress,email_adress,number):
        self.name = name 
        self.surname = surname
        self.adress = adress
        self.email_adress = email_adress
        self.number = number
        
    def __str__(self):
        return f"{self.name}  {self.surname},  {self.email_adress}"
    
    def contact(self):
        return f"Kontaktuję się z: {self.name} {self.surname}, pod numerem {self.number}) "
    
    @property
    def letters_length(self):
        return sum([len(self.name), len(self.surname)])    

persone_one = BaseContacts(name='James',surname='Murphy',adress='1089 Maple Court',email_adress='JamesMMurphy@teleworm.us',number="501-727-8175")
persone_two = BaseContacts(name='Nicola',surname='Smith',adress='300 Colony Street',email_adress='ReneeCGranados@jourrapide.com',number="415-412-9260")
persone_three = BaseContacts(name='William',surname='Brooks',adress='2873 Quiet Valley Lane',email_adress='WilliamRBrooks@rhyta.com',number="508-381-3285")
person_four = BaseContacts(name='Noe',surname='Folk',adress='293 Hanover Street',email_adress='NoeTFalk@armyspy.com',number="951-572-1817")
person_five = BaseContacts(name='Ilona',surname='Kowalska',adress='2 Powsy Sike',email_adress='DavidGMcFarland@jourrapide.com',number="559-304-525")
print(persone_three.letters_length)
print(persone_three.contact())


class BusinessContact(BaseContacts):
    def __init__(self,occupation,company_name,phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company_name = company_name
        self.phone_number = phone_number
    
    def contact(self):
        return f"Kontaktuję się z: {self.name} {self.surname}, pod numerem {self.phone_number},nazwa firmy {self.company_name}) "
    
    @property
    def letters_length(self):
        return sum([len(self.name), len(self.surname)])  
    
persone_1 = BusinessContact(name='Ola',surname='Kowalska',adress='2657 Edgewood Avenue',email_adress='AllanSVance@armyspy.com',number='123-345-678',occupation='Keypunch operator',company_name='Total Quality',phone_number='4536-7689-798')
print(persone_1.contact())
print(persone_1.letters_length)
    



#persona_1 = BaseContacts(first_name=fake.name(), last_name=fake.surname(), company=fake.company_name(), position=fake.occupation(),
#             email_address=fake.email_adress(), phone_number=fake.phone_number())