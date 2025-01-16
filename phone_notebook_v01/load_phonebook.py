import json
import os
import config

# path to JSON
PHONEBOOK_FILE = config.DATABASE_NAME

# Loading or creating the phonebook
def load_phonebook():
    """Function, that checks if some data exist in folder
    and loads them if yes"""
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'r') as file:
            return json.load(file)
    else:
        print(f"FILE {PHONEBOOK_FILE} NOT FOUND! PLEASE CREATE A NEW PHONEBOOK.\n", "-" * 40, sep='')
        return {'contacts': []}