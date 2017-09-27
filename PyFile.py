import csv
import os
import sys
import getpass

usr_dat = ".usr_dat"
new_usr_var = "NewUser"
new_pas = "Admin12"
term_prompt = "$ "

help_text = """Help:
edit [file name] | Opens file for edit or, if ther is no file found, creates new file
exit | Exits PyFile
about | Information about PyFile
list | Lists all files under user (ls shortcut)
setting | not working right now
mkdir | make a folder
cd | Changes the current directory.
delete [file name] | deletes the specified file."""

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
            print("That user alredy exists.")

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
path_str = "/Main"
while not exit:
    command = input(usr + path_str + term_prompt)
    if command != "":
        if os.path.exists(command):
            os.system("python3 " + command)
        else:
            command = command.lower()
            if command == "exit":
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
                print(help_text)
            elif command == "about":
                print()
                print("About:")
                print("Created By: Hayden S, Hunter C, and Max S")
                print("v")
            elif command[:5] == "mkdir":
                dirname = command[6:]
                os.mkdir(dirname)
            elif command[:2] == "cd":
                if os.path.isdir(command[3:]):
                    if command[3:] == "../":
                        path_table = path_str.split("/")
                        if len(path_table) > 2:
                            path_str = "/"
                            for i in range(len(path_table) - 1):
                                if i > 1:
                                    path_str = path_str + "/" + path_table[i]
                                else:
                                    path_str = path_str + path_table[i]
                            os.chdir(command[3:])
                    else:
                        path_str = path_str + "/" + command[3:]
                        os.chdir(command[3:])
                else:
                    print("Directory does not exsist. Use mkdir.")
            elif command[:6] == "delete":
                if os.path.exists(command[7:]) and not os.path.isdir(command[7:]):
                    confirm = input("Conformation (Y/N): ")
                    if confirm.lower() == "y" or confirm.lower() == "yes" or confirm.lower() == "ya":
                        try:
                            os.remove(command[7:])
                        except:
                            print("Error deleting file.")
                    else:
                        print("Delete canceled.")
                elif os.path.exists(command[7:]) and os.path.isdir(command[7:]):
                    try:
                        os.rmdir(command[7:])
                    except:
                        print("Directory is not empty.")
                else:
                    print("File does not exist.")
            else:
                print("That is not a command please type 'help' to get help with commands.")
