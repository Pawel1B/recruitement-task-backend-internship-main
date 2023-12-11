
class User:

    def __init__(self, firstName:str, telephone_number:int, email:str, password:str, role:str, created_at, children:list):
        self.__firstName=firstName
        self.__telephone_number=telephone_number
        self.__email=email
        self.__password=password
        self.__role=role
        self.__created_at=created_at
        self.__children=children


    def login(self, password_sent):
        if password_sent==self.__password:
            return True, self.__role
        else:
            print("Wrong password for user: "+self.__email)
            return False, self.__role

    def get_firstName(self):
        return self.__firstName
    def get_telephone_number(self):
        return self.__telephone_number
    def set_telephone_number(self, telephone_number):
        self.__telephone_number=telephone_number
        pass
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_role(self):
        return self.__role
    def get_createdAt(self):
        return self.__created_at
    def get_children(self):
        return self.__children