from twilio.rest import Client
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

try:
    f = open("spam.txt", "r")
    auth = f.read()
    f.close
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("spam.txt", "w")
    f.write(wr)
    f.close
    f = open("spam.txt", "r")
    auth = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests
	
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
    s = int(input("\033[1;0;40mEnter Amount - "))
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
    again()

def off():
    ss = 0
    mm = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get( client, message)
        resp = str(res)
        if resp == '<Response [204]>':
            print(bar)
            print("\n\033[1;32;40m [+] Sending Fail ... [+]")
            print("\n\033[1;32;40m cheak send sandbox message")
            print(bar)
        elif resp == '<Response [200]>':
            mm = mm + 1
            print(bar)
            print("\n\033[1;32;40m [+] Send Successfull")
            print(bar)
        else:
            print(bar)
            print("\n\033[1;31;40m [+] Not connect Sandbox Thus Number")
            print(bar)


        ss+=1
        print("\033[1;0;40m\n",str(ss)," kin ",str(mm), "Goda....  Eelaga >")
        for i in range(180):

            pr = i/180*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")

            time.sleep(0.5)
            sys.stdout.write("\033[F")

    os.system('figlet FINISHED')
    again()

def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
