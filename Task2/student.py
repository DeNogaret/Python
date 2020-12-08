class Student(object):
    __name: str
    __gender: str
    __age: int
    __phone: str

    def __init__(self, name: str):
        self.__name = name

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_gender(self, gender: str):
        self.__gender = gender

    def get_gender(self) -> str:
        return self.__gender

    def set_age(self, age: int):
        self.__age = age

    def get_age(self) -> int:
        return self.__age

    def set_phone(self, phone: str):
        self.__phone = phone

    def get_phone(self) -> str:
        return self.__phone

    def output(self):
        print('______________________________')
        print(
            f'Name: {self.get_name()} '
            f'\nPhone: {self.get_phone()} '
            f'\nAge: {self.get_age()}'
            f'\nGender: {self.get_gender()}'
        )
        print('______________________________')
