from createsend import *


account_auth = {'api_key':'/7k+rgSybkxGMa64aUb+DPuAGpM5NxC3EjanNlSDjrRom3gKTHe6Z/t5GOJA9IlditAvifnjymZGVH6ZW1xqYE5EnuoJBr9hWXn7yscIZOyoeoJjugUcGix/fb8V2lzJIG+ab56sLijjsgL49KGvWw=='}
client_auth = {'api_key':'otYR1hX2Rwul5NfryE/34LF2dpnEq54yCYn3ezdGVsEx5m6Ii3JJ0xp1+RpBPsnD2M3Nw7O2fkWTfZTFhGsK6YfZ2bFe2q/f0BVMLC1M08x45xlTEi3KSzjzASFxtxp0Wlepoi9SVYr6ga/vF7bd4A=='}


account_admin=CreateSend(account_auth)

tz_list=account_admin.timezones()

country_list=account_admin.countries()

client_list=account_admin.clients()

print(client_list[0].ClientID)

client_dict={}

for client in client_list:
    client_dict[client.Name] = client.ClientID

print(client_dict['Advanced - Automotive'])

#print(my_names[0])

#print(names[0])


#print(type(client_list))
#for c in client_list:
    #print(dir(c))

#for c in country_list:
#    print(c)

#for t in tz_list:
#    print(t)




#my_list = List(client_auth)

#my_list.create("2bd21ec1091ba743b483563a25062a61", "API List 4", "", False, "")


#my_subscriber = Subscriber(client_auth)

#custom_fields = [{"Key": 'website', "Value": 'http://example.com/'}]

#my_subscriber.add("7c480b336839fbba731ca50c5d269666", "jashton+api3@sailthru.com", "Subscriber", custom_fields, True, "yes")

#my_client = Client(account_auth)

#my_client.create("ZZ API Test Client", "(GMT-05:00) Eastern Time (US & Canada)", "United States of America")
