#this program has all functionalities needed for solving tasks, with the use of sorted data entities

def print_all_accounts(data):
    print(len(data))

def print_oldest_account(data):
    def myKey(s):
        return s.get_createdAt()
    data_2=data.copy()
    data_2.sort(key=myKey)
    oldest=data_2[0]
    print("name: "+oldest.get_firstName())
    print("email_address: "+oldest.get_email())
    print(f"created_at: {oldest.get_createdAt()}")

def group_children_by_age(data):
    children_list=[]
    for user in data:
        if user.get_children()!=[]:
            for child in user.get_children():
                children_list.append(child)
    def myKey(s):
        return -s.get_age()
    children_list.sort(key=myKey)
    age=children_list[0].get_age()
    counter=0
    counters=[]
    ages=[age]
    for index, child in enumerate(children_list):
        if age==child.get_age():
            counter+=1
        else:
            counters.append(counter)
            age=child.get_age()
            ages.append(child.get_age())
            counter=1
        if index==len(children_list)-1:
            counters.append(counter)
    sort_list=[]
    for index, item in enumerate(counters):
        sort_list.append([item, ages[index]])
    sort_list.sort()
    for counter, age in (sort_list):
        print("age: "+str(age)+", count: "+str(counter))

def print_children(user_data):
    children_list=user_data.get_children()
    if children_list==[]:
        print("No children assigned to this user")
    else:
        def myKey(s):
            return s.get_name()[0]
        children_list.sort(key=myKey)
        for child in children_list:
            print(child.get_name()+", "+str(child.get_age()))

def find_similar_children_by_age(user_data, data):
    ages_to_find=[]
    children=user_data.get_children()
    if children==[]:
        print("No children assigned to this user")
    else:
        for child in children:
            ages_to_find.append(child.get_age())
    result_data=[]
    for user in data:
        children_found=[]
        for child in user.get_children():
            if child.get_age() in ages_to_find:
                children_found.append([child.get_name(), child.get_age()])
        if children_found!=[]:
            result_data.append([user.get_firstName(), user.get_telephone_number(), children_found])
    for result in result_data:
        children_str=""
        children_found=result[2]
        for index, child_data in enumerate(children_found):
            children_str+=(f'{child_data[0]}, {child_data[1]}')
            if index<len(children_found)-1:
                children_str+='; '
        print(result[0]+", "+str(result[1])+": "+children_str)