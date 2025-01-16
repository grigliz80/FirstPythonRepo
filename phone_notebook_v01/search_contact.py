def search_contact(phonebook):
    """SEARCH. Function is searching a contact by parameter"""
    search_type = input('SEARCH BY (first_name, last_name, phone, country): ').strip()
    search_value = input('ENTER VALUE TO SEARCH: ').strip()

    results = [c for c in phonebook['contacts'] if search_value.lower() in str(c.get(search_type, '')).lower()]
    if results:
        print("SEARCH RESULT: ")
        for contact in results:
            print(f"{contact['first_name']} {contact['last_name']} - {contact['phone']} ({contact['country']})")
    else:
        print("CONTACT NOT FOUND\n", "-" * 40, sep='')