#User Timing time
class UserFocusTimingSetup :
    #Timing Setup of user
    def __init__(self):
        self.__userWakeUpTimeInHours = 0        
        self.__userWakeUpTimeInMinutes = 0
        self.__userSleepTimeInHours = 0
        self.__userSleepTimeInMinutes = 0
        self.__userApproxFocusTimingStartHours = 0
        self.__userApproxFocusTimingStartMinutes = 0
        self.__userApproxFocusTimingEndHours = 0
        self.__userApproxFocusTimingEndMinutes = 0
        self.__userApproxFocusHours = 0
        
    # Wake up time by user
    def setWakeupTime(self,wakeUpInHour, wakeupInMin):
        self.__userWakeUpTimeInHours = wakeUpInHour
        self.__userWakeUpTimeInMinutes = wakeupInMin
    # Sleep time by user
    def setSleepTime(self,sleepInHours, sleepInMin):
        self.__userSleepTimeInHours = sleepInHours
        self.__userSleepTimeInMinutes = sleepInMin
    # Focus time by user
    def setFocusTime(self,focusStartHours,focusStartMin, focusEndHour, focusEndMin, approxNeedFocusHours):
        self.__userApproxFocusTimingStartHours = focusStartHours
        self.__userApproxFocusTimingStartMinutes = focusStartMin
        self.__userApproxFocusTimingEndHours = focusEndHour
        self.__userApproxFocusTimingEndMinutes = focusEndMin
        self.__userApproxFocusHours = approxNeedFocusHours

        
    #User time setup    
    def UserTimingSetup(self):  
        while True:
            print("\n\t 1) Set the wakeup timings")
            print("\n\t 2) Set the sleep timings")
            print("\n\t 3) Set focus timings")
            print("\n\t 4) Edit timings")
            
            choice = int(input("\n\tPlease enter your choice: "))
            match choice :
                case 1 :
                    while True :
                        wakeUpHour = int(input("\n\t Please enter the wakeup timings in hours : "))
                        wakeUpMin = int(input("\n\t Please enter the wakeup timings in minutes : "))
                    
                        if(wakeUpHour<=0 or wakeUpMin<=0 or wakeUpMin>60 or wakeUpHour>24 ):
                            print("\n\tInvalid choice!!!")
                        else :
                            self.setWakeupTime(wakeUpHour, wakeUpMin)
                            break
                case 2 :
                    while True :
                        sleepHours = int(input("\n\t Please enter the sleep timings in hours : "))
                        sleepMin = int(input("\n\t Please enter the sleep timings in minutes : "))
                        if(sleepHours<=0 or sleepHours > 24 or sleepMin <= 0 or sleepMin >60):
                            print("\n\tInvalid choice!!!")
                        else:
                            self.setSleepTime(sleepHours, sleepMin)
                            break
                case 3 :
                    while True :
                        focusStartInHours = int(input("\n\t Please enter the focus start timing in hours : "))
                        focusStartInMin = int(input("\n\t Please enter the focus start timing in minutes : "))
                        focusEndHours = int(input("\n\t Please enter the focus end timings in hours : "))
                        focusEndMin = int(input("\n\t Please enter the focus end timing in minutes : "))
                        approxFocus = int(input("\n\t Please enter the focus end timing in hours(Approx): "))
                        if(focusStartInHours <=0 or focusStartInHours > 24 or focusEndMin <= 0 or focusEndMin > 60 or focusStartInMin <=0 
                           or focusStartInMin > 60 or focusEndHours <= 0 or focusEndMin > 60 or approxFocus <= 0 or approxFocus > 60):
                            print("\n\tInvalid choice!!!")
                        else :
                            self.setFocusTime(focusStartInHours, focusStartInMin, focusEndHours, focusEndMin, approxFocus)
                            break
                
                case 4:
                    print("\n\t Re-edit all those things")
                    continue
                
                case 5:
                    print("\n\tDone!!")
                    break
                
                case _:
                    print("Please Enter valid choice!!!")
                    continue
                
#Focus session display
#     def getTimings(self):
#                 print("\n\tWakeup time: ",self.__userWakeUpTimeInHours," : ", self.__userWakeUpTimeInMinutes)
#                 print("\n\tSleep time: ",self.__userSleepTimeInHours," : ",self.__userSleepTimeInMinutes)
#                 print("\n\tFocus time start: ",self.__userApproxFocusTimingStartHours," : ",self.__userApproxFocusTimingStartMinutes)
#                 print("\n\tFocus time end: ",self.__userApproxFocusTimingEndHours," : ",self.__userApproxFocusTimingEndMinutes)
#                 print("\n\tFocus time: ",self.__userApproxFocusHours)               
             
                
# sev = UserFocusTimingSetup()
# sev.UserTimingSetup()
# sev.getTimings()

    