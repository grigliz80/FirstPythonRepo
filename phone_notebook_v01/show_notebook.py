def show_phonebook(phonebook):
    """VIEW. Function, that shows all contacts in phonebook"""
    if phonebook['contacts']:
        for contact in phonebook['contacts']:
            print(f"{contact['first_name']} {contact['last_name']} - {contact['phone']} ({contact['country']})")
    else:
        print("THE PHONEBOOK IS EMPTY")
    print("-" * 40)