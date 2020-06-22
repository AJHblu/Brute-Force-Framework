import os
import time
import sentry_sdk
sentry_sdk.init("https://43f47ed836314db497d1fb037e3c4ef3@o410599.ingest.sentry.io/5285693")

os.system("sudo apt-get install git -y")
os.system("sudo apt-get isntall snapd")
os.chdir("/usr/share/")

print("""
 ___             _            ___ 
| _ ) _ _  _  _ | |_  ___    | __| ___  _ _  __  ___
| _ \| '_|| || ||  _|/ -_)   | _| / _ \| '_|/ _|/ -_)
|___/|_|   \_._| \__|\___|   |_|  \___/|_|  \__|\___|
 ___                                            _   
| __| _ _  __ _  _ __   ___  _ __ __  ___  _ _ | |__
| _| | '_|/ _` || '  \ / -_) \ V  V // _ \| '_|| / /
|_|  |_|  \__/_||_|_|_|\___|  \_/\_/ \___/|_|  |_\_\\

By: https://github.com/AJHblu
""")
time.sleep(1)

while True:
    os.system("clear")
    print("""
    \\______________Coded by: AJHblu______________/

    [1] dirbusting
    [2] web based
    [3] pass the hash
    [4] list generator
    [99] exit 
    """)
    option = input("BFFRAMEWORK~# ").strip()

    if option == "1":
        os.system("clear")
        os.system("sudo apt-get install dirb")
        while True:
            print("""
            \\______________Dirbusting______________/

            [1] simple attack
            [2] custom wordlist
            [99] back
            """)
            option = input("BFFRAMEWORK~# ").strip()
            if option == '1':
                url = input("Website url example http://url.domain/directory/: ")
                if url is not None:
                    os.system(f"dirb {url}")
                else:
                    os.system("clear")
                    print("please enter a url")
                    time.sleep(1)
            elif option == '2':
                url = input("Website url example http://url.domain/directory/: ")
                wordlist = input("Path to wordlist: ")
                if url is not None:
                    if wordlist is None:
                        print("using default wordlist")
                        os.system(f"dirb {url}")
                    else:
                        print(f"atempting to use {wordlist}")
                        os.system(f"dirb {url} {wordlist}")
            elif option == '99':
                print("exiting")
                time.sleep(1)
                break
            else:
                os.system("clear")
                print("not a valid option")
                time.sleep(1)


    elif option == "2":
        os.system("clear")
        os.system("sudo apt-get install hydra")
        while True:
            print("""
            \\______________WEB______________/

            [1] simple attack (-l -P)
            [2] reverse attack (-L -p)
            [99] back
            """)
            option = input("BFFRAMEWORK~# ").strip()
            if option == '1':
                url = input("Website url example http://url.domain/directory/: ")
                wordlist = input("Path to wordlist(used for passwords): ")
                user = input("Enter username: ")
                if url is not None:
                    if wordlist is not None:
                        if user is not None:
                            os.system(f"hydra -l {user} -P {wordlist} {url}")
                        else:
                            os.system("clear")
                            print("please enter a username")
                            time.sleep(1)
                            os.system("clear")
                    else:
                        os.system("clear")
                        print("please enter a wordlist")
                        time.sleep(1)
                        os.system("clear")  
                else:
                    os.system("clear")
                    print("please enter a url")
                    time.sleep(1)
                    os.system("clear")

            elif option == '2':
                url = input("Website url example http://url.domain/directory/: ")
                wordlist = input("Path to wordlist(used for usernames): ")
                password = input("Enter password: ")
                if url is not None:
                    if wordlist is not None:
                        if password is not None:
                            os.system(f"hydra -L {wordlist} -p {password} {url}")
                        else:
                            os.system("clear")
                            print("please enter a password")
                            time.sleep(1)
                            os.system("clear")
                    else:
                        os.system("clear")
                        print("please enter a wordlist")
                        time.sleep(1)
                        os.system("clear")  
                else:
                    os.system("clear")
                    print("please enter a url")
                    time.sleep(1)
                    os.system("clear")

            elif option == '99':
                print("exiting")
                time.sleep(1)
                os.system("clear")
                break

            else:
                os.system("clear")
                print("not a valid option")
                time.sleep(1)

    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "99":
        print("exiting")
        break
    else:
        os.system("clear")
        print("please enter a valid option")
        time.sleep(1)