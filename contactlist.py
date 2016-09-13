




class ContactList(list):





    def search(self, looking_for):
        matching_items = []
        for contact in self:
            if looking_for == contact.name:
                matching_items.append(contact)
        return matching_items
