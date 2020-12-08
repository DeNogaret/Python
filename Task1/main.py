from contact import Contact
from phone_book import PhoneBook

print("Phone book")

phoneBook = PhoneBook()


def show_all(phone_book: PhoneBook):
    if phone_book.get_count() == 0:
        print("No contacts in phone book. Please add.")
        return

    for contact in phone_book.get_contacts():
        print(
            f'Name: {contact.get_name()} '
            f'\nMobile Phone: {contact.get_mob_phone()} '
            f'\nPersonal Phone: {contact.get_personal_phone()}'
            f'\nAbout contact: {contact.get_description()}'
        )
        print('______________________________')

def add_contact(phone_book: PhoneBook):
    name = input("Input name of contact: ")
    contact = Contact(name)

    contact.mob_phone = input("Input Mobile Phone: ")
    contact.personal_phone = input("Input Personal Phone: ")
    contact.description = input("Describe contact: ")

    phone_book.add_contact(contact)

    print("Contact successfully added")


def delete_contact(phone_book: PhoneBook):
    name = input("Input name of contact which you want to delete: ")

    contact = phone_book.find_contact(name)

    if contact is not None:
        phone_book.delete_contact(contact)
        print("Contact deleted")

while 1:
    command = input("Input number of menu: \n1:Show all contacts, \n2:Add contact to Phone Book, \n3:Delete contact \n")

    switcher = {
        "1": show_all,
        "2": add_contact,
        "3": delete_contact,
    }

    func = switcher.get(command, "nothing")

    func(phoneBook)
