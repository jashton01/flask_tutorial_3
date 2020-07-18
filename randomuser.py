'''


url = "https://randomuser.me/api/"

r = requests.get(url = url)

data = r.text

print(data)
'''
import requests
import random

from createsend import Subscriber, Client, CreateSend, List
a_test_client_auth = {'api_key':'lD25bbPMG56nPb6mtaJPxiP7bryKppJXB39hpNBS8CT2vJyJ8eULOl6hks7OCuqYP9iGzyLzcmwTddM66R+pRf41MMlwpIl0DRLPXeTFe97AldcFtEG+iApWgMWvFBDRPi57xA4XZ1kpCQIMPeh1PQ=='}

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



'''
my_subscriber = Subscriber(a_test_client_auth)

subscribers = [{"EmailAddress":"subscriber5@example.com","Name":"New Subscriber One","CustomFields":[{"Key":"website","Value":"http://example.com"},{"Key":"interests","Value":"magic"},{"Key":"interests","Value":"romantic walks"},{"Key":"age","Value":"","Clear":True}],"ConsentToTrack":"Yes"},{"EmailAddress":"subscriber2@example.com","Name":"New Subscriber Two","ConsentToTrack":"No"},{"EmailAddress":"subscriber3@example.com","Name":"New Subscriber Three","ConsentToTrack":"Unchanged"}]
'''
my_subscriber = Subscriber(a_test_client_auth)
my_subscriber.import_subscribers("5926ac888cffa2665144bae9127a89a5", subscriber_list, True, False, True)
