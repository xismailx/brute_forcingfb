import fbchat
from getpass import getpass
username = str(raw_input("Username: "))
password = str(raw_input("Pass: "))
client = fbchat.Client(username, password)
no_of_friends = int(raw_input("Number of friends: "))
victim = str(raw_input("Id of victim: "))
