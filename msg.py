import fbchat
from getpass import getpass
username = str(raw_input("Username: "))
password = str(raw_input("Pass: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends: "))
for i in xrange(no_of_friends):
    name = str(raw_input("Name: "))
