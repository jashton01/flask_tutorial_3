import config
import requests
import random

from createsend import Subscriber, Client, CreateSend, List
a_test_client_auth = config.a_test_client_auth
account_auth = config.account_auth

def create_new_list(clientid, list_name="Main List 7"):
    my_list = List(account_auth)
    list_id=my_list.create(clientid, list_name, "", False, "")
    return list_id

def create_custom_fields(field_name,options,list_id="2345accabd471c4c45e5fc463c8353a1"):
    my_list = List(account_auth,list_id)
    create_custom_fields = my_list.create_custom_field(field_name=field_name,data_type="MultiSelectOne",options=options,visible_in_preference_center=True)

#new_list_id=create_new_list(clientid="ae803b630f09179e016db499a401fdc6")

#print("Your list ID is" + new_list_id)

#print(create_custom_fields)

def print_random_name():
    url = "https://randomuser.me/api?results=5&nat=us,gb"
    r = requests.get(url = url)
    data = r.json()
    #print(data)
    return(data)


# my_client = Client(account_auth)
# client_lists = my_client.lists()
# print(client_lists)



my_names=print_random_name()

print(my_names)


test_field_name="Main Hobby"
possible_interests=["getting drunk","playing cards","rollerblading"]

#fields_created = create_custom_fields(field_name=test_field_name,options=possible_interests)
#print("You created the following entry" + fields_created)

def create_subscriber_list():
    subscriber_list=[]
    for i in my_names['results']:
        print(i['name']['first']+" "+i['name']['last'])
        random_subscriber={}
        random_subscriber.update(Name = i['name']['first']+" "+i['name']['last'])
        random_subscriber.update(EmailAddress = i['email'])
        random_subscriber.update(ConsentToTrack = "Yes")
        random_subscriber.update(CustomFields = [{"Value":random.choice(possible_interests),"Key":test_field_name}])
        #print(random_subscriber)
        subscriber_list.append(random_subscriber)
        #print("sub list in function: " + subscriber_list)
    return subscriber_list

subscriber_list=create_subscriber_list()
print(subscriber_list)

#print(subscriber_list)
#create_new_list(clientid="9cde80d058d8e4955a076d33b6ec2294")

print(subscriber_list)
my_subscriber = Subscriber(account_auth)
my_subscriber.import_subscribers("2345accabd471c4c45e5fc463c8353a1", subscriber_list, True, False, True)
