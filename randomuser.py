import config
import requests
import random

from createsend import Subscriber, Client, CreateSend, List
a_test_client_auth = config.a_test_client_auth
account_auth = config.a_test_client_auth




def create_new_list(clientid, list_name="Main List"):
    my_list = List(account_auth)
    my_list.create(clientid, list_name, "", False, "")


def print_random_name():
    url = "https://randomuser.me/api?results=5&nat=us,gb"
    r = requests.get(url = url)
    data = r.json()
    #print(data)
    return(data)

#def get_main_list():

my_client=Client(a_test_client_auth)
client_lists = my_client.lists()
print(client_lists)


'''
my_names=print_random_name()

random_subscriber={}
subscriber_list=[]

possible_interests=["getting drunk","playing cards","rollerblading"]

for i in my_names['results']:
    print(i['name']['first']+" "+i['name']['last'])
    random_subscriber={}
    random_subscriber.update(Name = i['name']['first']+" "+i['name']['last'])
    random_subscriber.update(EmailAddress = i['email'])
    random_subscriber.update(ConsentToTrack = "Yes")
    random_subscriber.update(CustomFields = [{"Key":"interests","Value":random.choice(possible_interests)}])
    subscriber_list.append(random_subscriber)


#print(subscriber_list)
#create_new_list(clientid="9cde80d058d8e4955a076d33b6ec2294")


my_subscriber = Subscriber(account_auth)
my_subscriber.import_subscribers("0561ad7fe4c247083dd71ca327bd1e1d", subscriber_list, True, False, True)
'''
