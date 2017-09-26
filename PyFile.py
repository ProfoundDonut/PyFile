
import csv
import os
import sys
import getpass

usr_dat = ".usr_dat"
new_usr_var = "NewUser"
new_pas = "Admin12"
term_prompt = "$"

path = ".term"
if os.path.exists(path) and os.path.isdir(path):
    print("Terminal path loaded.")
else:
    print("Terminal path not foud, creating terminal path.")
    os.mkdir(path)
    print("Terminal path loaded.")
os.chdir(path)

def write(x,y):
    with open(x, 'w') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(r) for r in sorted(y)]

def read(x):
    with open(x, 'r') as csvfile:
        reader = csv.reader(csvfile)
        table = [[str(e) for e in r] for r in reader]
    return table

def login(x,y,usr_dat,new_usr_var,new_pas):
    try:
        read(usr_dat)
    except:
        write(usr_dat,[[new_usr_var,new_pas]])
    usr_dat = read(usr_dat)
    for i in range(len(usr_dat)):
        if usr_dat[i][0] == x and usr_dat[i][1] == y:
            return x
    return "nil"

def new_usr(usr_dat,new_usr_var,new_pas):
    try:
        read(usr_dat)
    except:
        write(usr_dat,[[new_usr_var,new_pas]])
    done = False
    while not done:
        table = read(usr_dat)
        usr = input("Enter New Username: ")
        found = False
        for i in range(len(table)):
            if table[i][0] == usr:
                found = True
        if not found:
            done1 = False
            while not done1:
                pas = getpass.getpass("Enter New Password: ")
                check_pas = getpass.getpass("Confirm New Password: ")
                if pas == check_pas:
                    table = table + [[usr,pas]]
                    write(".usr_dat", table)
                    print("New User Created!")
                    done1 = True
                    done = True
                else:
                    print("Password not consistant.")
        else:
            print("That user alredy exsists.")


is_logged_in = False
while not is_logged_in:
    usr = login(input("Enter Username: "), getpass.getpass("Enter Password: "), usr_dat,new_usr_var,new_pas)
    if usr == "nil":
        print("Invalid username or password.")
    elif usr == new_usr_var:
        new_usr(usr_dat,new_usr_var,new_pas)
    else:
        is_logged_in = True


path = "." + usr + "_dat"
if os.path.exists(path) and os.path.isdir(path):
    print("User path loaded.")
else:
    print("User path not foud, creating user path.")
    os.mkdir(path)
    print("User path loaded.")
os.chdir(path)

exit = False
while not exit:
    command = input(usr + term_prompt)
    if command != "":
        if os.path.exists(command):
            os.system("python3 " + command)
        elif command == "exit":
            os._exit(1)
        elif command[:4] == "edit":
            if os.path.exists(command[5:]):
                os.system("nano "+command[5:])
            else:
                open(command[5:], 'w').close()
                os.system("nano "+command[5:])
        elif command == "ls" or command == "list":
            table = os.listdir()
            for i in range(len(table)):
                print(table[i])
        elif command == "help":
            print()
            print("Help:")
            print("edit [file name] | Opens file for edit or, if ther is no file found, creates new file")
            print("exit | Exits PyFile")
            print("about | Information about PyFile")
            print("list | Lists all files under user (ls shortcut)")
            print("setting | ")
        elif command == "about":
            print()
            print("About:")
            print("Created By: Hayden S, Hunter C, and Max S")
            print("v")
