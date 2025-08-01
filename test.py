def updateGreeting(func):


    def runDecorator():
        print("Decorator is running")
        print("Welcome to the class this morning")


    def getAnotherGreeting():
        print("This is another greeting")
   

    result = func()
    if result == 1:
        return runDecorator
    else: 
        return getAnotherGreeting
    




@updateGreeting
def greetUser():
    print("Welcome to the class")
    return 1
    

greetUser()