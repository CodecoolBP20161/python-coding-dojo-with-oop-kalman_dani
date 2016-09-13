from contact import *
from supplier import *


# supplier = Supplier('Bela', 'kissbela@valami')
# supplier.order('halll')
#
# print(Supplier.all_orders)
#
# list_1 = ContactList()
# list_1.append(45)
# print(list_1)
# list_1.clear()
#
# print(Contact.all_contacts)

Dani = Contact('Dani', 'dani@kukac')
Dani = Contact('Dani', 'dani@kukac')
Dani = Contact('Dani', 'dani@kukac')
Miki = Contact('Miki', 'miki@miki')


print(Contact.all_contacts.search('Dani'))
