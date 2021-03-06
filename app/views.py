import config
account_auth = config.account_auth
client_auth = config.client_auth
a_test_client_auth = config.a_test_client_auth

from app import app
from flask import render_template
from flask import request, redirect
from flask import jsonify, make_response
from createsend import Subscriber, Client, CreateSend, List
#from createsend import Client
#from createsend import Administrator
#from createsend import CreateSend


def create_new_list(clientid, list_name="Main List"):
    my_list = List(account_auth)
    my_list.create(clientid, list_name, "", False, "")

def get_clients():
    account_admin=CreateSend(account_auth)
    client_list=account_admin.clients()
    return client_list

def client_name_id(client_list):
    clients_and_ids = {}
    for client in client_list:
        clients_and_ids[client.Name] = client.ClientID
    return clients_and_ids

def add_subscriber(username):
    my_subscriber = Subscriber(client_auth)
    custom_fields = [{"Key": 'username', "Value": username}]
    my_subscriber.add("7c480b336839fbba731ca50c5d269666", "jashton+api8@sailthru.com", username, custom_fields, True, "yes")
    print("success")

def add_client(prospect_name, prospect_tz):
    my_client = Client(account_auth)
    my_client.create(prospect_name, prospect_tz, "United States of America")


def print_random_name():
    url = "https://randomuser.me/api?results=5&nat=us,gb"
    r = requests.get(url = url)
    data = r.json()
    #print(data)
    return(data)

def create_new_list(client_id, list_name):
    my_list = List(account_auth)
    my_list.create(client_id, list_name, "", False, "")

def list_names(client_id):
    my_client=Client(account_auth, client_id=client_id)
    results=my_client.lists()
    list_names_dir={}
    list_names=[]
    for r in results:
        list_names_dir[r.Name]=r.ListID
        list_names.append(r.Name)
    print(list_names)
    if 'Main List' not in list_names:
        print("it's not there!")
        create_new_list(client_id=client_id, list_name="Main List")
    else:
        print("we see it!")
    #return(list_names_dir['Main List'])

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/client_create", methods=["GET", "POST"])
def client_create():
    my_clients = get_clients()
    clients_and_ids = client_name_id(my_clients)
    return render_template("public/client_create.html", my_clients=my_clients, clients_and_ids=clients_and_ids)

@app.route("/client_create/create_client", methods=["POST"])
def create_client():
    req = request.get_json()
    print(req)
    prospect_name = req['client_name']
    prospect_tz = req['client_tz']
    add_client(prospect_name=prospect_name,prospect_tz=prospect_tz)
    res = make_response(jsonify(req), 200)
    return res

@app.route("/client_create/create_lists_and_subs", methods=["POST"])
def create_list():
    req = request.get_json()
    #print(req)
    client_id = req['client_name']
    #list_name = req['list_name']
    custom_field_name = req['custom_field_name']
    custom_field_value1 = req['custom_field_value1']
    custom_field_value2 = req['custom_field_value2']
    custom_field_value3 = req['custom_field_value3']
    #print("Client ID: ",client_id," Custom Field Name: ",custom_field_name)
    list_names(client_id=client_id)
    #new_list=create_new_list(clientid=client_id,list_name="Main List 8")
    #print("type of new list: ", length(new_list))
    res = make_response(jsonify(req), 200)
    print(res)
    return res


#adding something

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form
        missing = list()
        for k, v in req.items():
            if v == "":
                missing.append(k)
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)

        req = request.form
        print("Your response is:", req)
        user_name = req['username']
        add_subscriber(username=user_name)
        return redirect(request.url)


    return render_template("public/sign_up.html")

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    res = make_response(jsonify(req), 200)

    return res

@app.route("/jinja")
def jinja():
    my_name = "Julian"

    # Integers
    my_age = 23

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    return render_template(
    "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
    friends=friends, colors=colors, cool=cool, GitRemote=GitRemote,
    my_remote=my_remote, repeat=repeat
)
