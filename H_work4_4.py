def add_contact(contacts, name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def parse_input(command):
    parts = command.split()
    if not parts:
        return None, None, None
    keyword = parts[0].lower()
    if keyword == "hello":
        return lambda x, y=None, z=None: print("How can I help you?"), None, None
    elif keyword == "add" and len(parts) == 3:
        return add_contact, parts[1], parts[2]
    elif keyword == "change" and len(parts) == 3:
        return change_contact, parts[1], parts[2]
    elif keyword == "phone" and len(parts) == 2:
        return show_phone, parts[1], None
    elif keyword == "all" and len(parts) == 1:
        return show_all, None, None
    elif keyword in {"close", "exit"}:
        return exit, None, None
    else:
        print("Invalid command.")
        return None, None, None



def main():
    contacts = {}

    while True:
        command = input("Enter command: ")
        handler, arg1, arg2 = parse_input(command)
        if handler:
            if handler == exit:
                print("Good bye!")
                break
            elif arg2 is not None:
                handler(contacts, arg1, arg2)
            elif arg1 is not None:
                handler(contacts, arg1)
            else:
                handler(contacts)

if __name__ == "__main__":
    main()
