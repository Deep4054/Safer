#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <limits>
using namespace std;

/*Loign class*/
class USER_MAIN_LOGIN
{
private:
    string user_local_password;

public:
    string user_full_name;
    string user_main_email;
    USER_MAIN_LOGIN()
    {
        user_full_name = "root";
        user_local_password = "root@123";
        user_main_email = "";
    }
    void set_details()
    {
        /*Taking Name*/
        cout << "\n\tPlease enter your full Name: ";
        getline(cin, user_full_name);
        while (user_full_name == "root") /*Check name is root or not */
        {
            cout << "Invalid! Please enter full name again: ";
            getline(cin, user_full_name);
        }
        /*Password Check*/
        cout << "\n\tPlease enter your local password: ";
        cin >> user_local_password;
        /*Check Email*/
        cout << "\n\tPlease enter your email: ";
        cin >> user_main_email;
        while (user_main_email == "") /*Email chcek*/
        {
            cout << "Invalid! Please enter email again: ";
            cin >> user_main_email;
        }
    }
    void show_details()
    {
        cout << "\n\tUser Full Name: " << user_full_name;
        cout << "\n\tUser Email Address: " << user_main_email;
        cout << "\n\tUser local password: " << user_local_password;
    }
};

/*Work and Goal Setup*/
class USER_WORK_INFORMATION
{
public:
    string user_current_role;
    vector<string> user_goal;

    /*Check and store profession*/
    void set_work_informatation()
    {
        while (1)
        {
            int choice;
            cout << "\n\t1) Student";
            cout << "\n\t2) Developer";
            cout << "\n\t3) Content Creator";
            cout << "\n\t4) Manager";
            cout << "\n\tPlease enter your choice in number: ";
            cin >> choice;
            if (choice == 1)
            {
                user_goal.push_back("Student");
                set_goal_student();
                break;
            }
            else if (choice == 2)
            {
                user_goal.push_back("Developer");
                break;
            }
            else if (choice == 3)
            {
                user_goal.push_back("Content Creator");
                break;
            }
            else if (choice == 4)
            {
                user_goal.push_back("Manager");
                break;
            }
            else
            {
                cout << "Please enter valid number !!";
            }
        }
    }

    void set_goal_student()
    {
        while (1)
        {
            int choice;
            /*Student Have multiple goals so loops runs multiple time*/
            cout << "\nSome goals for student";
            cout << "\n\t1) Learner";
            cout << "\n\t2) Skill oriented Developer";
            cout << "\n\t3) Placement-Oriented";
            cout << "\n\t4) Collaborator";
            cout << "\n\t5) Exit";
            cout << "\n\tPlease enter your choice in number: ";
            cin >> choice;
            if (choice == 1)
            {
                user_current_role = "Learner";
            }
            else if (choice == 2)
            {
                user_current_role = "Skill oriented Developer";
            }
            else if (choice == 3)
            {
                user_current_role = "Placement-Oriented";
            }
            else if (choice == 4)
            {
                user_current_role = "Collaborator";
            }
            else if (choice == 5)
            {
                if (user_current_role.empty())
                    user_current_role = "Unspecified";
                break;
            }
            else
            {
                cout << "Please enter valid number !!";
            }
        }
    }
};

/*Collage Details setup*/
class USER_COLLEGE_DETAILS
{
private:
    /*Private Information*/
    int user_college_year;
    int user_college_starting_year;
    int user_college_ending_year;
    string highest_education;

public:
    /*Setting the value*/
    void set_college_info()
    {
        while (1)
        {
            int choice;
            cout << "\n\t1) SSC or below";
            cout << "\n\t2) HSC";
            cout << "\n\t3) Bachelor";
            cout << "\n\t4) Other above Bachelor";
            cout << "\n\tPlease select choice: ";
            cin >> choice;

            if (choice == 1)
            {
                highest_education = "S.S.C or below";
                user_college_starting_year = 0;
                user_college_ending_year = 0;
                user_college_year = 0;
                break;
            }
            else if (choice == 2)
            {
                highest_education = "H.S.C";
                user_college_starting_year = 0;
                user_college_ending_year = 0;
                user_college_year = 0;
                break;
            }
            else if (choice == 3 || choice == 4)
            {
                /*If Both are graduate so ask them collage specification*/
                if (choice == 3)
                    highest_education = "Bachelor";
                else
                    highest_education = "Other above Bachelor";

                while (true)
                {
                    cout << "\n\tPlease enter your starting college year: ";
                    cin >> user_college_starting_year;
                    cout << "\n\tPlease enter your ending college year: ";
                    cin >> user_college_ending_year;

                    if (user_college_ending_year <= user_college_starting_year)
                    {
                        cout << "\n\t⚠️ Invalid year range. Try again.\n";
                    }
                    else
                    {
                        user_college_year = user_college_ending_year - user_college_starting_year;
                        /*Break Here*/
                        break;
                    }
                }
                break;
            }
            else
            {
                cout << "\n\t⚠️ Please enter correct number (1 to 4 only).\n";
            }
        }
    }
};

/*Time and min setup*/
class USER_FOCUS_SETUP
{
public:
    /*Setting Times*/
    vector<string> user_mood;
    int user_echo_wake_up_time_hour;
    int user_echo_wake_up_time_min;
    int user_echo_sleep_time_hour;
    int user_echo_sleep_time_min;
    int user_focus_timing_duration_hour;
    int user_focus_start_time_hours;
    int user_focus_start_time_min;
    int user_focus_end_time_hours;
    int user_focus_end_time_min;

    /*Default Counstructor*/
    USER_FOCUS_SETUP()
    {
        user_echo_wake_up_time_hour = 0;
        user_echo_wake_up_time_min = 0;
        user_echo_sleep_time_hour = 0;
        user_echo_sleep_time_min = 0;
        user_focus_timing_duration_hour = 0;
        user_focus_start_time_hours = 0;
        user_focus_start_time_min = 0;
        user_focus_end_time_hours = 0;
        user_focus_end_time_min = 0;
    }

    void user_mood_setup()
    {
        while (1)
        {
            int choice = 100;
            cout << "\n\t1) User Mood";
            cout << "\n\t2) Set Wake up time";
            cout << "\n\t3) Set sleep time";
            cout << "\n\t4) Set Focus time duration";
            cout << "\n\t5) Exit";
            cout << "\n\tPlease enter your choice: ";
            cin >> choice;

            if (choice == 1)
            {
                while (true)
                {
                    int choice_mood;
                    cout << "\n\tChoose your mood status:";
                    cout << "\n\t1)  Excited";
                    cout << "\n\t2)  Fulfilled";
                    cout << "\n\t3)  Exit";
                    cout << "\n\tYour choice: ";
                    cin >> choice_mood;

                    switch (choice_mood)
                    {
                    case 1:
                        user_mood.push_back("Excited");
                        cout << "\n\tMood added: Excited ";
                        break;
                    case 2:
                        user_mood.push_back("Fulfilled");
                        cout << "\n\tMood added: Fulfilled ";
                        break;
                    case 3:
                        cout << "\n\tExiting mood input... \n";
                        break;
                    default:
                        cout << "\n\tInvalid choice! Please enter 1, 2, or 3.\n";
                        continue;
                    }

                    if (choice_mood == 3)
                        break;
                }
            }
            else if (choice == 2)
            {
                /*Wake Up TImings*/
                do
                {
                    cout << "\n\tEnter wake-up hour (0-23): ";
                    cin >> user_echo_wake_up_time_hour;
                } while (user_echo_wake_up_time_hour < 0 || user_echo_wake_up_time_hour > 23);

                do
                {
                    cout << "\n\tEnter wake-up minutes (0-59): ";
                    cin >> user_echo_wake_up_time_min;
                } while (user_echo_wake_up_time_min < 0 || user_echo_wake_up_time_min > 59);
            }
            else if (choice == 3)
            {
                /*User Sleep Hours*/
                do
                {
                    cout << "\n\tEnter sleep hour (0-23): ";
                    cin >> user_echo_sleep_time_hour;
                } while (user_echo_sleep_time_hour < 0 || user_echo_sleep_time_hour > 23);

                do
                {
                    cout << "\n\tEnter sleep minutes (0-59): ";
                    cin >> user_echo_sleep_time_min;
                } while (user_echo_sleep_time_min < 0 || user_echo_sleep_time_min > 59);
            }
            else if (choice == 4)
            {
                cout << "\n\tEnter focus duration hour: ";
                cin >> user_focus_timing_duration_hour;
                cout << "\n\tEnter focus start hour: ";
                cin >> user_focus_start_time_hours;
                cout << "\n\tEnter focus start min: ";
                cin >> user_focus_start_time_min;
                cout << "\n\tEnter focus end hour: ";
                cin >> user_focus_end_time_hours;
                cout << "\n\tEnter focus end min: ";
                cin >> user_focus_end_time_min;
            }
            else if (choice == 5)
            {
                break;
            }
            else
            {
                cout << "\n\tInvalid choice! Try again !";
            }
        }
    }
};

/*Favorite Platform Setup*/
class USER_USAGE_FAVORITE_PLATFORM_DETAILS
{
public:
    string user_favorite_platform;
    string platform_link;
    int user_platform_wise_limit_hours;
    int user_platform_wise_limit_min;
    int user_total_use_of_platform;
    int user_minimum_blocking_time_platform_wise;

    USER_USAGE_FAVORITE_PLATFORM_DETAILS()
        : user_favorite_platform(""), platform_link(""),
          user_platform_wise_limit_hours(0), user_platform_wise_limit_min(0),
          user_total_use_of_platform(0), user_minimum_blocking_time_platform_wise(0) {}

    USER_USAGE_FAVORITE_PLATFORM_DETAILS(string fav_patform, string link, int total_use_hour, int total_use_min, int minimum_blocking)
    {
        user_favorite_platform = fav_patform;
        platform_link = link;
        user_platform_wise_limit_hours = total_use_hour;
        user_platform_wise_limit_min = total_use_min;
        user_minimum_blocking_time_platform_wise = minimum_blocking;
    }

    vector<string> user_fav_site_switch_time_duration;
    vector<string> user_fav_platform_time_spent_per_day;
};

/*Distructive Platform Setup*/
class USER_USAGE_DESTRUCTIVE_PLATFORM_DETAILS
{
public:
    string user_destructive_platform_block_status;
    string user_destructive_platform;
    string platform_link;
    int user_minimum_blocking_time_platform_wise_hours;
    int user_minimum_blocking_time_platform_wise_min;

    USER_USAGE_DESTRUCTIVE_PLATFORM_DETAILS() {}

    USER_USAGE_DESTRUCTIVE_PLATFORM_DETAILS(string destructive_platform, string block_status, string link, int blocking_time_hour, int blocking_time_min)
    {
        user_destructive_platform_block_status = block_status;
        user_minimum_blocking_time_platform_wise_hours = blocking_time_hour;
        platform_link = link;
        user_destructive_platform = destructive_platform;
        user_minimum_blocking_time_platform_wise_min = blocking_time_min;
    }
};

/*Hidden class Subject and extrenal links*/
class USER_PLANNING_SETUP
{
    /*Just As a Hidden class*/
public:
    int user_number_of_subjects;
    vector<string> external_links;
};

/*Subjects of students stored*/
class SUBJECT_INFORMATION
{
public:
    /*Hidden class object called*/
    USER_PLANNING_SETUP planning_Setup;

    /*Alll Setup in main class*/
    string user_subject_name;
    vector<string> subject_wise_material_links;
};

/*Output report genrator*/
class USER_OUTPUT_REPORT
{
public:
    /*Report form as pdf or word file*/
    string user_output_report_format;
    void user_output_report()
    {
        int choice;
        while (1)
        {
            cout << "\n\t1) PDF";
            cout << "\n\t2) Word";
            cout << "\n\tPlease enter the report format: ";
            cin >> choice;
            if (choice == 1)
            {
                user_output_report_format = "PDF";
                break;
            }
            else if (choice == 2)
            {
                user_output_report_format = "Word";
                break;
            }
            else
            {
                cout << "\n\tPlease Enter valid choice !!!";
            }
        }
    }
};

/**Main Class**/
class USER_PROFILE
{
public:
    USER_MAIN_LOGIN login;
    USER_WORK_INFORMATION work_information;
    USER_COLLEGE_DETAILS user_college_information;
    USER_FOCUS_SETUP focus_setup;
    vector<USER_USAGE_FAVORITE_PLATFORM_DETAILS> user_favorite_platform_details;
    vector<USER_USAGE_DESTRUCTIVE_PLATFORM_DETAILS> user_destructive_platform_details;
    vector<SUBJECT_INFORMATION> subject_details;
    USER_OUTPUT_REPORT user_output;
};

int main()
{
    USER_PROFILE first_person;
    first_person.login.set_details();
    first_person.login.show_details();
}