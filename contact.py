from contactlist import *

class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = ContactList()
