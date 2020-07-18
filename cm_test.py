import config
from createsend import Subscriber, Client, CreateSend, List


account_auth = config.account_auth
client_auth = config.client_auth
a_test_client_auth = config.a_test_client_auth

#my_lists=Client(client_auth)
#lists_in_account=my_lists.lists()

#for l in lists_in_account:
#    print(l)

#my_client = Client(account_auth)
#my_client.create("ZZZ API Test Client", "(GMT-05:00) Eastern Time (US & Canada)", "United States of America")
'''
account_admin=CreateSend(account_auth)
client_list=account_admin.clients()
#print(client_list[0])


clients_and_ids = {}
for client in client_list:
    clients_and_ids[client.Name] = client.ClientID
    #print(clients_and_ids[key])

#print(clients_and_ids)


account_admin=CreateSend(account_auth)

tz_list=account_admin.timezones()

country_list=account_admin.countries()

for c in country_list:
    print(c)
'''
#for t in tz_list:
#    print(t)




my_list = List(account_auth)

#my_list.create("9cde80d058d8e4955a076d33b6ec2294", "July 13 v8", "", False, "")
#print(my_list.list_id)


my_subscriber = Subscriber(a_test_client_auth)
'''
my_custom_fields = [{"Key": "Favorite Cuisine", "Value": "Pizza"},{'Key': 'Hobby', "Value": "Football"}]

new_custom_fields = [{"Key": "things i love", "Value": "new york"}, {"Key": "things i also love", "Value": "coding"}, {"Key": "things i hate", "Value": "watching tv"}]


#my_subscriber.add("5926ac888cffa2665144bae9127a89a5", "jashton+api4@sailthru.com", "Subscriber", my_custom_fields, True, "yes")

my_subscriber.add("5926ac888cffa2665144bae9127a89a5", "jashton+api5@sailthru.com", "Subscriber", new_custom_fields, True, "yes")
'''

subscribers = [{"EmailAddress":"subscriber1@example.com","Name":"New Subscriber One","CustomFields":[{"Key":"website","Value":"http://example.com"},{"Key":"interests","Value":"magic"},{"Key":"interests","Value":"romantic walks"},{"Key":"age","Value":"","Clear":True}],"ConsentToTrack":"Yes"},{"EmailAddress":"subscriber2@example.com","Name":"New Subscriber Two","ConsentToTrack":"No"},{"EmailAddress":"subscriber3@example.com","Name":"New Subscriber Three","ConsentToTrack":"Unchanged"}]

my_subscriber.import_subscribers("5926ac888cffa2665144bae9127a89a5", subscribers, True, False, True)
