####dont know####

class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, username):
        self.name = name
        self.username = username


class Network:
    # Define the fields and methods for your object here.
    def __init__(self, list_users):
        self.list_users = []
        # self.user.append(user)
    def add_friends(self, friend):
        self.add_friends.append(friend)

def main():
    # Define the program flow for your user interface here.
    real_name = input("What's your name?  ")
    user_name = input("What's your username?  ")
    while user_name in list_users:
        user_name = input("%s already exits. What's your username?  " %(user_name))


    user1 = User(real_name, user_name)
    # user2.add_user(user_name)

# Runs your program.
if __name__ == '__main__':
    main()
####dont know####
