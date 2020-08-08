import config

from createsend import Subscriber, Client, CreateSend, List

a_test_client_auth = config.a_test_client_auth
account_auth = config.account_auth

def create_new_list(clientid, list_name):
    my_list = List(account_auth)
    my_list.create(clientid, list_name, "", False, "")

def list_names(client_id):
    my_client=Client(a_test_client_auth, client_id=client_id)
    results=my_client.lists()
    list_names_dir={}
    list_names=[]
    for r in results:
        list_names_dir[r.Name]=r.ListID
        list_names.append(r.Name)
    if 'Main List' not in list_names:
          create_new_list(clientid=client_id)
    return(list_names_dir['Main List'])

# my_client=Client(account_auth, client_id="9cde80d058d8e4955a076d33b6ec2294")
#
# client_details = my_client.details()
#
# print(client_details.ApiKey)



#print(a_test_client_auth)

# #print("hello world")
#
# my_subscriber = Subscriber(a_test_client_auth)
#
# my_custom_fields = [{"Key": "Favorite Cuisine", "Value": "Pizza"},{'Key': 'Hobby', "Value": "Football"}]
#
# my_subscriber.add("5926ac888cffa2665144bae9127a89a5", "jashton+api6@sailthru.com", "Subscriber", my_custom_fields, True, "yes")
#
my_client=Client(account_auth, client_id="9cde80d058d8e4955a076d33b6ec2294")
results=my_client.lists()
list_names_ids={}
list_names=[]
for r in results:
    list_names_ids[r.Name]=r.ListID
    list_names.append(r.Name)

print(list_names)
if 'Main List' not in list_names:
    print("its not there")
else:
    print("It exists!")
#
#
# print(type(dir(results[0])))
#
# print(type(results[0]))
#
# print([r.Name, r.ListID for r in results])
