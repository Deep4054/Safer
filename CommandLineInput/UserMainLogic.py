import getpass # sefty of password

##User Main profile module
class UserMainLogic:
    def __init__(self):
        #Private password 
        self.__userLocalPassword = "root@123"
        
        #Public methods
        self.userFullName ="root"
        self.userMailAddress =""
    
    # Setting up the data from user
    def setDetails(self):
        self.userFullName =input("\n\tPlease enter your full Name: ")
            
        # User name must not root
        while self.userFullName == "root":
            self.userFullName = input("\n\tInvalid! Please enter full name again: ")
            
        #Password inputs
        self.__userLocalPassword = getpass.getpass("\n\tPlease enter your local password: ") #Taken imput as hidden
        
        #Email inputs
        self.userMailAddress = input("\n\t Please enter email: ")
        
        #check empty input is given by user
        while self.userMailAddress == "":
            self.userMailAddress = input("\n\tInvalid!, Please enter email: ")

    #display function (optional to use)
    def showDetails(self):
        print("\n\tUser full name: "+self.userFullName)
        print("\n\tUser Email address: "+self.userMailAdress)
        print("\n\tUser local password: "+self.__userLocalPassword)
