#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

/*User main classes declartaion*/

/*User main login information class*/
class USER_MAIN_LOGIN
{
private:
    vector<string> user_full_name;
    vector<string> user_main_email;
    vector<string> user_local_password;
};

/*User Education information and work information*/
class USER_WORK_INFORMATION
{
    vector<string> user_current_role;
    vector<string> user_goal;
};

/*If user is a collage student so get details of user*/
class USER_COLLAGE_DETAILS
{
    vector<string> user_collage_year;
    vector<string> user_collage_starting_year;
    vector<string> user_collage_ending_year;
};
/*User information details and mood setups*/
class USER_FOCUS_SETUP
{
    vector<string> user_mood;
    vector<string> user_echo_wake_up_time;
    vector<string> user_echo_sleep_time;
    vector<string> user_focus_timing_duration;
    vector<string> user_focus_start_time;
    vector<string> user_focus_end_time;
};

/*Usage tracking detils*/
class USER_USAGE_TRACKING
{
    vector<string> user_favorite_platform;
    vector<string> platform_link;
    vector<string> user_unfavorite_platform;
    vector<string> user_unfavourite_platform_block_status;
    vector<string> user_platform_wise_limt_hours;
    vector<string> user_total_use_of_platformp;
    vector<string> user_minimum_blocking_time_platform_wise;
    vector<string> user_fav_site_switch_recomandation;
    vector<string> user_fav_site_mush_switch_for_mins;
    vector<string> user_fav_platform_time_spent_per_day;
};

/*User planning setup*/
class USER_PLANNING_SETUP
{
    vector<int> user_number_of_subjects;
    vector<string> week_wise_time_table;
    vector<string> subject_wise_material_links;
    vector<string> external_links;
};

/*User otuput reports*/
class USER_OUTPUT_REPORT
{
    vector<string> user_output_report_formate;
};

/*Over all user object*/
class USER_PROFILE
{
    /*Object creation for each classes*/
    USER_MAIN_LOGIN login;
    USER_WORK_INFORMATION work_information;
    USER_COLLAGE_DETAILS user_collage_information;
    USER_FOCUS_SETUP focus_setup;
    USER_USAGE_TRACKING user_usege;
    USER_PLANNING_SETUP user_setup;
    USER_OUTPUT_REPORT user_output;
};