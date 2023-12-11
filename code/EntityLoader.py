from entities.User import User
from entities.Child import Child
from DataLoader import DataLoader, get_string_between
from datetime import datetime
# entity_loader is a functional file in which verification of loaded data is performed to desired entity classes and standards

def validate_email(email):
    first= email.count('@') == 1
    second = len(email.split('@')[0])>0
    third = len(get_string_between(email, '@', '.'))>0
    dot_sentence_length=len(email.split('.')[-1])
    fourth = email[-dot_sentence_length:].isalnum() and (dot_sentence_length>0 and dot_sentence_length<5)
    if first and second and third and fourth:
        return True
    else:
        return False


class EntityLoader:
    def __init__(self, directory_path="../data"):
        self.directory_path=directory_path



    def load_entities(self):
        data_loader=DataLoader(directory_path=self.directory_path)
        data=data_loader.load_data()
        final_data=[]
        phone_numbers=[]
        for index, user_data in enumerate(data):
            if validate_email(user_data[2]):
                if type(user_data[1])==str:
                    phone_number_str=user_data[1].replace(" ", "")
                    phone_number_start_index=len(phone_number_str)-9
                    phone_number=phone_number_str[phone_number_start_index:]
                    phone_number=int(phone_number)
                    final_data.append([user_data[0], phone_number, user_data[2], user_data[3], user_data[4], datetime.strptime(user_data[5], '%Y-%m-%d %H:%M:%S'), user_data[6], index])
        def myKey(s):
            return s[1]
        final_data.sort(key=myKey)
        old_phone=0
        sublist=[]
        phones_for_sublist=[]
        to_delete=[]
        for index, data in enumerate(final_data):
            if data[1] in phones_for_sublist:
                sublist.append(data)
            else:
                def myKey(s):
                    return s[5]
                sublist.sort(key=myKey)
                if len(sublist)>1:
                    for item in sublist[:-1]:
                        to_delete.append(item[7])
                sublist=[data]
                phones_for_sublist.append(data[1])
            old_phone=data[1]

        to_delete.sort()
        result=[]
        def myKey(s):
            return s[7]
        final_data.sort(key=myKey)
        for index, item in enumerate(final_data):
            if not index in to_delete:
                children=[]
                for item_1 in item[6]:
                    child=Child(item_1[0], int(item_1[1]))
                    children.append(child)
                user=User(item[0], item[1], item[2], item[3], item[4], item[5], children)
                result.append(user)
        return result