
# User Work information module
class UserWorkInformation :
    
# Counstructor of the module
    def __init__(self):
        self.userCurrentRole = ""
        self.userGoal=set()

    # Work information function
    def SetWorkInformation(self):
    
    # When choice matches the loop terminate
    
     while 1:
        print("\n\t1) Student")
        print("\n\t2) Developer")
        print("\n\t3) Content Creator")
        print("\n\t4) Manager")
        choice = int(input("\n\tPlease enter your choice in number: "))
        
        # control statement for user
        if choice == 1 :
            self.userCurrentRole = "Student"
            break
        elif choice ==2:
            self.userCurrentRole = "Developer"
            break
        elif choice == 3:
            self.userCurrentRole ="Content Creator"
            break
        elif choice == 4:
            self.userCurrentRole ="Manager"
            break
        else :
            print("\n\tPlease Enter valid choice: ")
    
    #goal information setup method
    def SetGoalInformation(self):
        
        while 1 :
            # choice selection
            print("\n\tPlease Enter choice: ")
            print("\n\t1) Learner")
            print("\n\t2) Developer")
            print("\n\t3) Job oriented")
            print("\n\t4) Free lanser")
            print("\n\t5) Exit")
            choice = int(input("\n\tPlease Enter your choice "))
            if choice == 1 :
                self.userGoal.append("Learner");
            elif choice == 2:
                self.userGoal.append("Developer");
            elif choice ==3:
                self.userGoal.append("Job oriented");
            elif choice ==4:
                self.userGoal.append("Free lanser");
            elif choice ==5:
                break
            else:
                print("\n\tPlease enter valid choice: ")
# Complete Module With some test cases
#     def show_info(self):
#         print("\n\tUser's Current goal: ",self.userGoal)
#         print("\n\tUser's Current Role: ",self.userCurrentRole)

# user = UserWorkInformation()
# user.SetWorkInformation()
# user.SetGoalInformation()
# user.show_info()
             
            
            

        


