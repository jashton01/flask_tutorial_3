import config
import requests
import random

from createsend import Subscriber, Client, CreateSend, List
a_test_client_auth = config.a_test_client_auth

def print_random_name():
    url = "https://randomuser.me/api?results=5&nat=us,gb"
    r = requests.get(url = url)
    data = r.json()
    #print(data)
    return(data)

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


print(subscriber_list)

my_subscriber = Subscriber(a_test_client_auth)
my_subscriber.import_subscribers("5926ac888cffa2665144bae9127a89a5", subscriber_list, True, False, True)
