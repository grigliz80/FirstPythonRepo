def update_contact(phonebook, ph_number):
    """UPDATE. Function, updating contact by tel number"""
    for contact in phonebook['contacts']:
        if contact['phone'] == ph_number:
            print(f"UPDATES FOR {contact['first_name']} {contact['last_name']}:")
            contact['first_name'] = input('ENTER NEW FIRST NAME (or press Enter to keep unchanged): ') or contact['first_name']
            contact['last_name'] = input('ENTER NEW LAST NAME (or press Enter to keep unchanged): ') or contact['last_name']
            contact['phone'] = input('ENTER NEW PHONE (or press Enter to keep unchanged): ') or contact['phone']
            contact['country'] = input('ENTER NEW COUNTRY (or press Enter to keep unchanged): ') or contact['country']
            print("CONTACT UPDATED\n", "-"*40, sep='')
            return
    print("CONTACT NOT FOUND\n", "-"*40, sep='')


def delete_contact(phonebook, ph_number):
    """DELETE. Function, deleting contact by tel number"""
    contacts_before = len(phonebook['contacts'])
    phonebook['contacts'] = [c for c in phonebook['contacts'] if c['phone'] != ph_number]
    if len(phonebook['contacts']) < contacts_before:
        print("CONTACT DELETED\n", "-"*40, sep='')
    else:
        print("CONTACT NOT FOUND\n", "-"*40, sep='')