class Contact:
    def __init__(self, name: str):
        self.name = name
        self.personal_phone = ''
        self.mob_phone = ''
        self.description = ''

    def set_mob_phone(self, mob_phone: str):
        self.mob_phone = mob_phone

    def set_personal_phone(self, phone: str):
        self.personal_phone = phone

    def set_description(self, description: str):
        self.description = description

    def get_personal_phone(self) -> str:
        return self.personal_phone

    def get_mob_phone(self) -> str:
        return self.mob_phone

    def get_description(self) -> str:
        return self.description

    def get_name(self) -> str:
        return self.name

    def __del__(self):
        print("Contact " + self.name + " removed")
