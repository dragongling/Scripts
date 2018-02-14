def incorrect_login_data():
    print("Combination of login and password is incorrect")


def print_error(message):
    print("Error: " + message)


def print_no_permission(permission_name):
    print_error("you have no " + permission_name + " permission for this file")


def print_usage(command, synoptics, description, example):
    print("Usage: " + command + synoptics + "\n" + description + "\nExample:\n\t" + command + example)


def check_permissions_and_execute(command_name, function):
    try:
        file_id = files.index(args[0])
        if rights.index(command_name) in rights_matrix[user_id][file_id]:
            function(file_id)
        else:
            print_no_permission(command_name)
    except ValueError:
        print_error("file not found")


def read(file_id):
    print(files_content[file_id])


def write(file_id):
    files_content[file_id] = " ".join(args[1:])
    print("Success!")


def check(login, password):
    try:
        user_id = users.index(login)
    except ValueError:
        incorrect_login_data()
        return -1
    if password != passwords[user_id]:
        incorrect_login_data()
        return -1
    return user_id


def ls(user_id):
    if not rights_matrix[user_id]:
        print("You don't have any rights in this system :(\nPlease contact with the system administrator")
    else:
        print("Available files:")
        for file_id in rights_matrix[user_id]:
            if not rights_matrix[user_id][file_id]:
                rights_string = "no rights"
            else:
                rights_string = ", ".join(rights[i] for i in rights_matrix[user_id][file_id])
            print("\t" + files[file_id] + ": " + rights_string)


class Command:
    def __init__(self, name):
        self.name = name


users = ["Alex", "Evgeny", "Vasiliy"]
passwords = ["123", "123", "123"]
files = ["Skynet.doc", "AI_research.7z", "Overwatch.exe"]
files_content = ["Skynet is a global computer system",
                 "AI will conquer the world!!!",
                 "Welcome to Overwatch, Soldier 78!"]
rights = ["read", "write", "grant"]
commands = ["read", "write", "grant", "exit", "quit"]
rights_matrix = [
    {0: [0, 1, 2], 1: [0, 1, 2], 2: []},
    {0: [0], 1: [1], 2: [2]},
    {}]


print("Welcome to Cyberdine Systems Inc.\nPlease, login into the system")
while True:
    login = input("Login: ")
    password = input("Password: ")
    user_id = check(login, password)
    if user_id == -1:
        continue
    print("Welcome, " + login)
    ls(user_id)
    while True:
        user_input = input(login.lower() + "@skynet:/$ ")
        command = user_input.split()[0]
        args = list(user_input.split()[1:])
        if command == "quit" or command == "exit":
            print("Goodbye, " + users[user_id])
            break
        elif command == "read":
            if len(args) != 1:
                print_usage("read", " FILE", "Reads content of the specific file", " file.txt")
            else:
                check_permissions_and_execute("read", read)
        elif command == "write":
            check_permissions_and_execute("write", write)
        elif command == "grant":
            if len(args) < 4:
                print_usage("grant", " USER RIGHTS... FILE",
                            "Grants selected user selected rights for the specific file", " user read write file.txt")
            else:
                eval("read(0)")
                username = args[0]
                filename = args[-1]
                rights = args[1:-1]
                print(username)
                print(filename)
                print(rights)
        else:
            print(command + ": command not found")
    break
