from twilio.rest import Client
import argparse
import sys
import os
import time
import urllib

os.system('clear')

bar = "\033[1;33;40m\n_________________________________________________\n"


name = """\033[1;32;40m
\t /$$$$$$$                  /$$ /$$   /$$             /$$
\t| $$__  $$                | $$| $$$ | $$            | $$ 
\t| $$  \ $$  /$$$$$$   /$$$$$$$| $$$$| $$  /$$$$$$  /$$$$$$ 
\t| $$$$$$$/ /$$__  $$ /$$__  $$| $$ $$ $$ /$$__  $$|_  $$_/
\t| $$__  $$| $$$$$$$$| $$  | $$| $$  $$$$| $$$$$$$$  | $$ 
\t| $$  \ $$| $$_____/| $$  | $$| $$\  $$$| $$_____/  | $$ /$$ 
\t| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$  |  $$$$/ 
\t|__/  |__/ \_______/ \_______/|__/  \__/ \_______/   \___/

\t [¤] Termux Whatsapp Spam
\t [¤] Versions : 2.0.
\t [¤] Coded By Shehan Lahiru
\t [¤] Credit Harshani Kumarasinhe
  """

print(name, "")

print("\033[0;36m "" ░P░A░N░D░O░R░A░")
print("\033[0;36m "" ")
print("\033[0;36m "" ωнαтsαρρ sραм")
print("")
print("\033[0;36m "" ")
t = input("Enter send message: ")
p = input("Enter a number: ")

def main():
    os.system("clear")
    print(name,"\n")
    account_sid = "ACccc5b0a8ad0202a78012e010bb926907"
    auth_token = "1feaef63b07744bbf6715ee212beb335"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         from_='whatsapp:+14155238886',
                         body= t,
                         to=p
                 )

    
    os.system('figlet END  PROGERAM')

if __name__ == "__main__":
    main()
