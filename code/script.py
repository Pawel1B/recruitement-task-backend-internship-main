from entities_services import *
from EntityLoader import EntityLoader
import argparse

def login_user(login, password, data):
    for user in data:
        if login == user.get_email() or login == user.get_telephone_number():
            return user.login(password), user

if __name__=="__main__":
    data=EntityLoader("./data").load_entities()
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name')
    parser.add_argument('--login')
    parser.add_argument('--password')
    args=parser.parse_args()
    function_name=str(args.function_name)
    login=args.login
    if len(login)==9 and login.isdigit():
        login=int(login)
    password=args.password
    login_result, user = login_user(login, password, data)
    login_status=login_result[0]
    role=login_result[1]
    if login_status==False:
        exit(0)
    else:
        if function_name == "print-all-accounts":
            if role=="admin":
                print_all_accounts(data)
            else:
                print("you need to be admin to access that option")
                exit(0)
        elif function_name == "print-oldest-account":
            if role == "admin":
                print_oldest_account(data)
            else:
                print("you need to be admin to access that option")
                exit(0)
        elif function_name == "group-by-age":
            if role == "admin":
                group_children_by_age(data)
            else:
                print("you need to be admin to access that option")
                exit(0)
        elif function_name == "print-children":
            print_children(user)
        elif function_name == "find-similar-children-by-age":
            find_similar_children_by_age(user, data)
        else:
            print("wrong function name")