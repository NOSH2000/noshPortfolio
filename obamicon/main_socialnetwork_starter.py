class User:
    # Define the fields and methods for your object here.

    def __init__(self, user_name,real_name):
    # variable SCOPE: parameter variables only exist inside their function
        self.username = user_name
        self.realname = real_name
        self.connections = [] #ready to connect with users
    # def __str__(self):
    #     return self.username.append(" ").append(self.realname)

class Network:
    def __init__(self):
        self.userlist = [] # ready to recieve new users

    def add_user(self, requested_name, real_name):
# this function will check if the username you chose has already been used
        for person in self.userlist: # check every user in the network
            if person.username == requested_name: #check if existing users already have this name
            # person.username refers to an existing object of type User
                print("This username is already taken")
                new_name = input("Please enter a new username")

        # create a new object of type User with the given credentials
        new_user = User(requested_name, real_name)
        self.userlist.append(new_user)

    def add_connection(self, user1, user2):
        #creates link between user1 and user2
        user1.connections.append(user2)
        user2.connections.append(user1)

    def print_users(self):
        # print every existing user
        for person in self.userlist:
            print(person.username)

    def print_connections(self, username):
        # print every connection for a specific user
        for connection in username.connections:
            print(connection)

def main():
    # Define the program flow for your user interface here.
    bazinga = Network()
    loop = True

    while loop == True:
        user_result = input('''
                                                            Welcome to BazZingA!
                You can create user (u), Print your connections or your friends (p), add friends (f), and view the user list(l)!
                                                    ~~~~Press C to close BazZingA~~~~

              ''')

        if user_result == 'u':
            real1_name = input("   What's your name?  ")
            user1_name = input("   What's your username?   ")
            # meggy = User(user1_name, real1_name)
            bazinga.add_user(user1_name, real1_name)

        elif user_result == 'p':
            base_user_name = input("    Which user's connection do you want to print?  ")
            for person in bazinga.userlist:
                if base_user_name == person.username:
                    base_user_name = person
            bazinga.print_connections(base_user_name)

        elif user_result == 'f':
            print(" To connect:-- ")
            user1 = input("      Type in your username:  ")
            user2 = input("      Type in your acquaintance's username:  ")
            for person in bazinga.userlist:
                if user1 == person.username:
                    user1 = person
                elif user2 == person.username:
                    user2 = person
            bazinga.add_connection(user1, user2)
            print("Congrats! Now you are connected to %s" %(user2.username))

        elif user_result == 'l':
            bazinga.print_users()

        elif user_result == 'c':
            loop = False

        else:
            user_result = input('''                                  !!ERROR!!
                    Create user (u), Print your connections or your friends (p), Add friends (f), View the user list(l)
                                                        ~~~~Press C to close BazZingA~~~~''')






        # megan = User("megan1", "Megan Kuo")
        # snap_cat.print_connections(megan)



# Runs your program.
if __name__ == '__main__':
    main()
