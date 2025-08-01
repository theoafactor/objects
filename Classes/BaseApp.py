class BaseApp:

    def __init__(self):
        self.username = None
        self.password = None
        print("Base App created")


    def loginUser(self, username, password):

        from Connection.users_database import users

        for user in users: 
            if user["username"] == username and user["password"] == password:
                print("User logged in succesfully!")
                self.username = username
                self.password = password
                break
        
        else: 
            print("User does not exist.")

        





