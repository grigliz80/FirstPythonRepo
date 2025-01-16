def create_contact(phonebook, f_name, l_name, ph_number, country):
    """NEW. Contact. Function< that adds new contact to phonebok"""
    phonebook['contacts'].append({
        'first_name': f_name,
        'last_name': l_name,
        'phone': ph_number,
        'country': country
    })
    print(f"CONTACT {f_name} {l_name} ADDED!\n", "-"*40, sep='')