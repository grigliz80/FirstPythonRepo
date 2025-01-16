"""The program will help you to create, review, search, delete and update
contacts."""

from create_contact import create_contact
from update_delete_contact import delete_contact
from load_phonebook import load_phonebook
from print_functionality import print_functionality
from show_notebook import show_phonebook
from save_phonebook import save_phonebook
from search_contact import search_contact
from update_delete_contact import update_contact

HEADER = 'WELCOME TO YOUR PERSONAL CONTACT MANAGER'

fuctions = [
    print_functionality,
    create_contact,
    show_phonebook,
    search_contact,
    delete_contact,
    update_contact
]


def main():
    print(HEADER, "\n", "-"*40, sep='')
    phonebook = load_phonebook()
    print_functionality()

    while True:
        choice = int(input('CHOSEN OPTION: '))

        if choice == 0:
            fuctions[choice]()
        elif choice == 1:
            answer = input('ENTER FIRST NAME, LAST NAME, TEL NUMBER, COUNTRY: ')
            f_name, l_name, ph_number, country = answer.split(', ')
            fuctions[choice](phonebook, f_name, l_name, ph_number, country)
        elif choice == 2:
            fuctions[choice](phonebook)
        elif choice == 3:
            fuctions[choice](phonebook)
        elif choice == 4:
            ph_number = input('ENTER TEL NUMBER TO DELETE: ')
            fuctions[choice](phonebook, ph_number)
        elif choice == 5:
            ph_number = input('ENTER TEL NUMBER TO UPDATE: ')
            fuctions[choice](phonebook, ph_number)
        elif choice == 6:
            save_phonebook(phonebook)
            print("DATA SET SAVED. EXIT...")
            break
        else:
            print("UNKNOWN OPTION. PLEASE TRY AGAIN.\n", "-"*40, sep='')


if __name__ == '__main__':
    main()
