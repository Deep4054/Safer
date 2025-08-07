import datetime

class UserPlatformDetails:
    """
    Class to manage user platform details for helpful and destructive (useless) platforms.
    Handles time limits, blocking, and permanent block management.
    """

    def __init__(self):
        # Helpful platforms and their URLs
        self.__userHelpfulPlatformAndLink = {}
        # Destructive (useless) platforms and their URLs
        self.__userDestructivePlatformAndLink = {}
        # Time limits for helpful sites
        self.__userHelpfulSiteTimeLimit = {}
        # Time limits for destructive sites
        self.__userStrictDestructivePlatformTimeLimit = {}
        # Minimum delay before switching from helpful platform
        self.__minimumHelpfulSwitchingDelay = {}
        # Minimum blocking delay for destructive platforms
        self.__minimumDestructiveBlockingTimeDelay = {}
        # Minimum blocking time for helpful platforms
        self.__minimumBlockingTimeUsefullPlatform = {}
        # Minimum blocking time for useless platforms
        self.__minimumBlockingTimeUseLessPlatform = {}
        # Max attempts to skip block for helpful platforms
        self.__maxAttemptsToSkipBlockUsefulPlatform = {}
        # Max attempts to skip block for useless platforms
        self.__maxAttemptsToSkipBlockUselessPlatform = {}
        # List of permanently blocked systems
        self.__permanentBlockedSystems = []

    def userPlatformDetails(self):
        """
        Main menu for user to input and manage platform details.
        """
        while True:
            print("\n\t1) Enter information of Helpful platform list")
            print("\n\t2) Enter information of Useless platform list")
            print("\n\t3) Manage permanent blocked systems")
            print("\n\t4) Exit")
            choice = input("\n\tPlease enter your choice: ")

            # Helpful site information
            if choice == "1":
                # Input helpful platform name
                usefulPlatform = input("\n\tEnter the useful website name: ")
                if usefulPlatform not in self.__userHelpfulPlatformAndLink:
                    self.__userHelpfulPlatformAndLink[usefulPlatform] = []

                # Add URLs for the helpful platform
                while True:
                    usefulPlatformLink = input("\n\tEnter the useful website URL: ")
                    if usefulPlatformLink not in self.__userHelpfulPlatformAndLink[usefulPlatform]:
                        self.__userHelpfulPlatformAndLink[usefulPlatform].append(usefulPlatformLink)
                        print("\n\tNew link added!!!")
                    else:
                        print("\n\tData is available!!!")

                    breakChoice = input("\n\tPress 1 to add more: ")
                    if breakChoice != "1":
                        break

                # Set daily time limit for this platform
                userHelpfulPlatformTImelimitHour = input("\n\tPlease Enter the daily time limit in hours for this platform: ")
                # (Note: This input is not used in logic)

                # Set safe time limit (hours and minutes)
                limitHours = int(input("\n\tSet time limit in hours (Safe limit): "))
                limitMinutes = int(input("\n\tSet time limit in minutes (Safe limit): "))
                timeLimit = datetime.time(limitHours, limitMinutes, 0)

                if timeLimit and usefulPlatform not in self.__userHelpfulSiteTimeLimit:
                    self.__userHelpfulSiteTimeLimit[usefulPlatform] = timeLimit

                # Initialize dictionaries for this platform if not exists
                if usefulPlatform not in self.__minimumHelpfulSwitchingDelay:
                    self.__minimumHelpfulSwitchingDelay[usefulPlatform] = []
                if usefulPlatform not in self.__minimumBlockingTimeUsefullPlatform:
                    self.__minimumBlockingTimeUsefullPlatform[usefulPlatform] = []
                if usefulPlatform not in self.__maxAttemptsToSkipBlockUsefulPlatform:
                    self.__maxAttemptsToSkipBlockUsefulPlatform[usefulPlatform] = 0

                # Set custom delay time (in minutes)
                customizeDelayTime = input("\n\tCustomise your delay time (must in minutes): ")
                if customizeDelayTime.isdigit():
                    self.__minimumHelpfulSwitchingDelay[usefulPlatform] = int(customizeDelayTime)
                    print(f"\n\tDelay time set to {customizeDelayTime} minutes")

                # Set max skip time (in minutes)
                maxTimeSkipPlatform = input("\n\tPlease add maximum time to skip platform (in minutes): ")
                if maxTimeSkipPlatform.isdigit():
                    self.__minimumBlockingTimeUsefullPlatform[usefulPlatform] = int(maxTimeSkipPlatform)
                    print(f"\n\tMaximum skip time set to {maxTimeSkipPlatform} minutes")

                # Set max attempts to skip blocking
                maxAttempts = input("\n\tSet maximum attempts to skip blocking for this platform: ")
                if maxAttempts.isdigit():
                    self.__maxAttemptsToSkipBlockUsefulPlatform[usefulPlatform] = int(maxAttempts)
                    print(f"\n\tMaximum skip attempts set to {maxAttempts}")

            # Useless platform list
            elif choice == "2":
                # Input useless platform name
                uselessPlatform = input("\n\tEnter the useless website name: ")
                if uselessPlatform not in self.__userDestructivePlatformAndLink:
                    self.__userDestructivePlatformAndLink[uselessPlatform] = []

                # Add URLs for the useless platform
                while True:
                    uselessPlatformLink = input("\n\tEnter the useless website URL: ")
                    if uselessPlatformLink not in self.__userDestructivePlatformAndLink[uselessPlatform]:
                        self.__userDestructivePlatformAndLink[uselessPlatform].append(uselessPlatformLink)
                        print("\n\tNew link added!!!")
                    else:
                        print("\n\tData is available!!!")

                    breakChoice2 = input("\n\tPress 1 to add more: ")
                    if breakChoice2 != "1":
                        break

                # Set warning time limit (hours and minutes)
                limitHours = int(input("\n\tSet time limit in hours (warning limit): "))
                limitMinutes = int(input("\n\tSet time limit in minutes (warning limit): "))
                timeLimit = datetime.time(limitHours, limitMinutes, 0)

                if timeLimit and uselessPlatform not in self.__userStrictDestructivePlatformTimeLimit:
                    self.__userStrictDestructivePlatformTimeLimit[uselessPlatform] = timeLimit

                # Initialize dictionaries for this platform if not exists
                if uselessPlatform not in self.__minimumDestructiveBlockingTimeDelay:
                    self.__minimumDestructiveBlockingTimeDelay[uselessPlatform] = 0
                if uselessPlatform not in self.__minimumBlockingTimeUseLessPlatform:
                    self.__minimumBlockingTimeUseLessPlatform[uselessPlatform] = 0
                if uselessPlatform not in self.__maxAttemptsToSkipBlockUselessPlatform:
                    self.__maxAttemptsToSkipBlockUselessPlatform[uselessPlatform] = 0

                # Set destructive platform blocking delay (in minutes)
                destructiveDelayTime = input("\n\tSet destructive platform blocking delay (in minutes): ")
                if destructiveDelayTime.isdigit():
                    self.__minimumDestructiveBlockingTimeDelay[uselessPlatform] = int(destructiveDelayTime)
                    print(f"\n\tDestructive blocking delay set to {destructiveDelayTime} minutes")

                # Set minimum blocking time for useless platform (in minutes)
                blockingTimeUseless = input("\n\tSet minimum blocking time for useless platform (in minutes): ")
                if blockingTimeUseless.isdigit():
                    self.__minimumBlockingTimeUseLessPlatform[uselessPlatform] = int(blockingTimeUseless)
                    print(f"\n\tMinimum blocking time set to {blockingTimeUseless} minutes")

                # Set max attempts to skip blocking for useless platform
                maxAttemptsUseless = input("\n\tSet maximum attempts to skip blocking for useless platform: ")
                if maxAttemptsUseless.isdigit():
                    self.__maxAttemptsToSkipBlockUselessPlatform[uselessPlatform] = int(maxAttemptsUseless)
                    print(f"\n\tMaximum skip attempts set to {maxAttemptsUseless}")

            # Permanent blocked systems management
            elif choice == "3":
                print("\n\t=== Permanent Blocked Systems Management ===")
                while True:
                    print("\n\t1) Add system to permanent block list")
                    print("\n\t2) Remove system from permanent block list")
                    print("\n\t3) View all permanently blocked systems")
                    print("\n\t4) Back to main menu")
                    subChoice = input("\n\tPlease enter your choice: ")

                    if subChoice == "1":
                        # Add system to permanent block list
                        systemToBlock = input("\n\tEnter system name to permanently block: ")
                        if systemToBlock not in self.__permanentBlockedSystems:
                            self.__permanentBlockedSystems.append(systemToBlock)
                            print(f"\n\t{systemToBlock} added to permanent block list")
                        else:
                            print(f"\n\t{systemToBlock} is already in permanent block list")

                    elif subChoice == "2":
                        # Remove system from permanent block list
                        if self.__permanentBlockedSystems:
                            print("\n\tCurrently blocked systems:")
                            for i, system in enumerate(self.__permanentBlockedSystems, 1):
                                print(f"\n\t{i}) {system}")
                            try:
                                removeIndex = int(input("\n\tEnter the number of system to remove: ")) - 1
                                if 0 <= removeIndex < len(self.__permanentBlockedSystems):
                                    removedSystem = self.__permanentBlockedSystems.pop(removeIndex)
                                    print(f"\n\t{removedSystem} removed from permanent block list")
                                else:
                                    print("\n\tInvalid selection")
                            except ValueError:
                                print("\n\tPlease enter a valid number")
                        else:
                            print("\n\tNo systems in permanent block list")

                    elif subChoice == "3":
                        # View all permanently blocked systems
                        if self.__permanentBlockedSystems:
                            print("\n\tPermanently blocked systems:")
                            for i, system in enumerate(self.__permanentBlockedSystems, 1):
                                print(f"\n\t{i}) {system}")
                        else:
                            print("\n\tNo systems in permanent block list")

                    elif subChoice == "4":
                        break
                    else:
                        print("\n\tPlease enter a valid number (1, 2, 3, or 4)")

            elif choice == "4":
                # Exit main menu
                break
            else:
                print("\n\tPlease enter a valid number (1, 2, 3, or 4)")

#     def printAllStoredData(self):
#         """
#         Print a summary of all stored data for helpful, destructive platforms, and permanent blocks.
#         """
#         print("\n" + "="*60)
#         print("\t\tALL STORED DATA SUMMARY")
#         print("="*60)

#         # Helpful Platforms Data
#         print("\n📚 HELPFUL PLATFORMS:")
#         print("-" * 40)
#         if self.__userHelpfulPlatformAndLink:
#             for platform, links in self.__userHelpfulPlatformAndLink.items():
#                 print(f"\n🔹 Platform: {platform}")
#                 print(f"   URLs: {', '.join(links)}")
#                 if platform in self.__userHelpfulSiteTimeLimit:
#                     print(f"   Time Limit: {self.__userHelpfulSiteTimeLimit[platform]}")
#                 if platform in self.__minimumHelpfulSwitchingDelay:
#                     print(f"   Switching Delay: {self.__minimumHelpfulSwitchingDelay[platform]} minutes")
#                 if platform in self.__minimumBlockingTimeUsefullPlatform:
#                     print(f"   Max Skip Time: {self.__minimumBlockingTimeUsefullPlatform[platform]} minutes")
#                 if platform in self.__maxAttemptsToSkipBlockUsefulPlatform:
#                     print(f"   Max Skip Attempts: {self.__maxAttemptsToSkipBlockUsefulPlatform[platform]}")
#         else:
#             print("   No helpful platforms added yet")

#         # Destructive Platforms Data
#         print("\n🚫 DESTRUCTIVE PLATFORMS:")
#         print("-" * 40)
#         if self.__userDestructivePlatformAndLink:
#             for platform, links in self.__userDestructivePlatformAndLink.items():
#                 print(f"\n🔹 Platform: {platform}")
#                 print(f"   URLs: {', '.join(links)}")
#                 if platform in self.__userStrictDestructivePlatformTimeLimit:
#                     print(f"   Warning Time Limit: {self.__userStrictDestructivePlatformTimeLimit[platform]}")
#                 if platform in self.__minimumDestructiveBlockingTimeDelay:
#                     print(f"   Blocking Delay: {self.__minimumDestructiveBlockingTimeDelay[platform]} minutes")
#                 if platform in self.__minimumBlockingTimeUseLessPlatform:
#                     print(f"   Min Blocking Time: {self.__minimumBlockingTimeUseLessPlatform[platform]} minutes")
#                 if platform in self.__maxAttemptsToSkipBlockUselessPlatform:
#                     print(f"   Max Skip Attempts: {self.__maxAttemptsToSkipBlockUselessPlatform[platform]}")
#         else:
#             print("   No destructive platforms added yet")

#         # Permanent Blocked Systems
#         print("\n🔒 PERMANENTLY BLOCKED SYSTEMS:")
#         print("-" * 40)
#         if self.__permanentBlockedSystems:
#             for i, system in enumerate(self.__permanentBlockedSystems, 1):
#                 print(f"   {i}. {system}")
#         else:
#             print("   No permanently blocked systems")

#         print("\n" + "="*60)

# # Example usage
# user = UserPlatformDetails()
# user.userPlatformDetails()
# user.printAllStoredData()