import os
from datetime import datetime, timedelta, timezone

def get_pakistan_time():
    utc_time = datetime.now(timezone.utc)
    pakistan_time = utc_time + timedelta(hours=5)
    print(f"The current date and time in Pakistan: {pakistan_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    get_pakistan_time()
file = open("pinfile.txt", "r")
pint = str(file.read())
file.close()
def main():
    for i in range(3):
        password = input('Enter Pin : ')
        j = 3
        if (password == pint) :
            print('Account Unlocked')
            mmenu = input("\n\n***********************\n\nWelcome To Billie Bank\n\n***********************\n\nEnter Your Desired Choice Below\n\n"
                              "(1) Deposit\n(2) Withdraw\n(3) Check Balance\n(4) Change Pin\n\n Enter Option : ")
            if mmenu == '1':

                    file = open("readfile.txt", "r")
                    balance = int(file.read())
                    deposit = int(input("Type Amount To Deposit : "))
                    balance = deposit + balance
                    file = open("readfile.txt", "w")
                    file.write(str(balance))

                    file = open("readfile.txt", "r")
                    content = file.read()
                    print(f'{content}$ Is Your Balance!')
                    file.close()
                    # repeat until user ends
                    foo = input('Enter 1 for MainMenu: ')
                    if foo == '1':
                        os.system('cls')
                        main()

            if mmenu == '2':
                    file = open("readfile.txt", "r")
                    balance = int(file.read())
                    withdraw = int(input("Type Amount To Withdraw : "))
                    if withdraw < balance or withdraw == balance:

                        balance = withdraw - balance
                        file = open("readfile.txt", "w")
                        file.write(str(balance))

                        file = open("readfile.txt", "r")
                        content = file.read()
                        print(f'{content}$ Is Your Balance After Withdrawal!')
                        file.close()
                        foo = input('Enter 1 for MainMenu: ')
                        if foo == '1':
                            os.system('cls')
                            main()


                    else:
                      print("the Amount can NOT Exceed Over Your Balance!")
                      foo = input('Enter 1 for MainMenu: ')
                      if foo == '1':
                          os.system('cls')
                          main()

            if mmenu == '3':
                    file = open("readfile.txt", "r")
                    content = file.read()
                    print(f'{content}$ Is Your Balance!\n')
                    file.close()
                    foo = input('Enter 1 for Main Menu: ')
                    if foo == '1':
                         os.system('cls')
                         main()
            if mmenu == '4':
                    newpin = input("Enter Your Desired Pin : ")
                    file = open("pinfile.txt", "w")
                    content = file.write(str(newpin))
                    print("\n**Operation Successful**")
                    file = open("pinfile.txt", "r")
                    contenttwo = file.read()
                    file.close()
                    print(f"\nYour New Pin Is {contenttwo} !")
                    break
        else:
            print(f"Incorrect Password, Remaining Chances are {j-i-1}")
            continue
    print(f"Account Is Now Locked!!")
main()