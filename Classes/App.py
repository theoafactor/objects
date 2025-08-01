from Classes.BaseApp import BaseApp

class App(BaseApp):
    
    def startApp(self):
        print("App started")

        ## ask for login details 
        username = input("Enter Username: ")
        password = input('Enter password: ')

        self.loginUser(username, password)

