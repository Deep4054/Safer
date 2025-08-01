class UserPlatformDetails:
    def __init__(self):
        self.__userHelpfulPlatformAndLink = {}
        self.__userDestructivePlatformAndLink = {}
        self.__userHelpfulSiteTimeLimit = {}
        self.__userStrictDestructivePlatformTimeLimit = {}
        self.__totalUsagePerSite = {}
        self.__minimumHelpfulSwitchingSuggestion = {}
        self.__minimumDestructiveBlockingTime = {} 
        self.__minimumBlockingTime = {}
        self.__maxAttemptsToSkipBlock = {}
        self.__permanentBlockedSystems =[]
        
    def setHelpfulWebsites(self):
        # Just loop until user enters
        while True:
            # Enter the user define choice
            print("\n\t1) Enter Helpful platform")
            print("\n\t2) Enter unuseful platform")
            print("\n\t3) Exit")
            choice = int(input("\n\tPlease enter the name and url of the platform : "))
            # switch cases for two types of sites suggestions
            match choice :
                
                # case 1 stands for Helpful  problem 
                case 1:
                    # Input title and forms
                    userHelpfulSite=input("\n\tPlease enter your Helpful sites (only title) : ")
                    
                    # Checks user string is not duplicates in dict 
                    if userHelpfulSite not in self.__userHelpfulPlatformAndLink :
                        self.__userHelpfulPlatformAndLink[userHelpfulSite] =[]
                    else :
                        print("\n\tYour Input is already present in data !!!")
                        
                    while(1):
                        # Enter working urls 
                        print("\n\t1) Enter Working URL")
                        print("\n\t2) Exit")
                        urlChoice = int(input("\n\tPlease enter the choice : "))
                        match urlChoice :
                            case 1:
                                inputUrl=input("Url: ")
                                if inputUrl not in self.__userHelpfulPlatformAndLink[userHelpfulSite] :
                                    self.__userHelpfulPlatformAndLink[userHelpfulSite].append(inputUrl);
                                else:
                                    print("\n\tUrl is already there!!!")
                            case 2:
                                break
                            case _:
                                print("\n\tPlease enter valid choice!!!")        
                # case 2 have same all the method as above test cases
                case 2:
                    useLessSites=input("\n\tPlease enter your useless sites (only title)")
                    if useLessSites not in self.__userDestructivePlatformAndLink :
                        self.__userDestructivePlatformAndLink[useLessSites] = []
                    else :
                        print("\n\tYour Input is already present in data !!!")
                        
                    while(1):

                        print("\n\t1) Enter Working URL")
                        print("\n\t2) Exit")
                        urlChoice = int(input("\n\tPlease enter the choice : "))
                        match urlChoice :
                            case 1:
                                inputUrl=input("Url: ")
                                if inputUrl not in self.__userDestructivePlatformAndLink[useLessSites] :
                                    self.__userDestructivePlatformAndLink[useLessSites].append(urlChoice);
                                else:
                                    print("\n\tUrl is already there!!!")
                            case 2:
                                break
                            case _:
                                print("\n\tPlease enter valid choice!!!")    
                case 3:
                    print("\n\t Good Website: ",self.__userHelpfulPlatformAndLink)
                    print("\n\t Harm ful website: ",self.__userDestructivePlatformAndLink)
                    break
                
                
User = UserPlatformDetails()
User.setHelpfulWebsites()