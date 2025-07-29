class UserCollegeInformation :
    
    # constructor for first initialization 
    def __init__(self):
        # self.userCollegeYear = 0 as a advance feature 
        self.userCollegeStartingYear =0
        self.userCollegeEndingYear =0
        self.highestEducationLevel =""
        
    # College degree year 
    def collegeYearDegree(self):
        
        while True :
            try:
                #Getting college year details
                self.userCollegeStartingYear = int(input("\n\tPlease enter your starting college year: "))
                self.userCollegeEndingYear = int(input("\n\tPlease enter your ending college year: "))

                # If else for college year detection
                if self.userCollegeEndingYear <= self.userCollegeStartingYear :
                    print("\n\tInvalid!!! Enter again")                
                else :
                    break
            except ValueError:
                print("\n\tEntered Value must be number !!")
                
    #College information
    def setCollegeInformation(self) :
        while True :
            print("\n\t1) SSC or below") 
            print("\n\t2) HSC")
            print("\n\t3) Bachelor")
            print("\n\t4) Other above Bachelor")
            
            #Throw Value error on return or takes any other things.
            try :
                choice=int(input("\n\tPlease select choice: "))
        
                #Switch case for selecting multiple from one
                match choice :
                    case 1:
                        self.highestEducationLevel ="S.S.C or below"
                        break
                    case 2:
                        self.highestEducationLevel="H.S.C"
                        break
                    case 3:
                        self.highestEducationLevel="Bachelor"
                        self.collegeYearDegree()
                        break
                    case 4:
                        self.highestEducationLevel="Other above Bachelor"
                        self.collegeYearDegree()
                        break
                    case _:
                        print("\n\tPlease enter valid choice")
                        
            except ValueError :
                print("\n\tEntered value must be Number!")
  
# THis code is only for testing purpose not for display anything      
#     def showUserDetails(self):
#         print("\n\tUser Education level: ",self.highestEducationLevel)
#         if self.userCollegeStartingYear == 0:
#             # do nothing
#             print("")
#         else :
#             print("\n\tUser college starting year: ",self.userCollegeStartingYear)
#             print("\n\tUser College ending year: ",self.userCollegeEndingYear)
            

# test = UserCollegeInformation()
# test.setCollegeInformation()
# test.showUserDetails()
            
        