#include <iostream>
#include <vector>
#include <string>
using namespace std;

// --- 1. Personal Info ---
class PersonalInfo
{
protected:
    string fullName;
    string email;
    string password;

public:
    void inputPersonalInfo()
    {
        cout << "Enter full name: ";
        getline(cin, fullName);
        cout << "Enter email (Gmail): ";
        getline(cin, email);
        cout << "Enter password: ";
        getline(cin, password);
    }

// --- 2. Education / Work Info ---
class EducationWorkInfo
{
protected:
    string currentRole;
    string collegeName;
    string studyYear;
    string focusGoal;

public:
    void inputEducationWork()
    {
        cout << "Enter current role (Student/Employee/Freelancer): ";
        getline(cin, currentRole);
        if (currentRole == "Student")
        {
            cout << "Enter college name: ";
            getline(cin, collegeName);
            cout << "Enter study year (First, Second, etc.): ";
            getline(cin, studyYear);
        }
        cout << "Enter focus/study goals: ";
        getline(cin, focusGoal);
    }

// --- 3. Focus Setup ---
class FocusSetup
{
protected:
    string mood;
    string wakeUpTime;
    string sleepTime;
    int workHours;

public:
    void inputFocusSetup()
    {
        cout << "Mood (Strict/Balanced/Chill): ";
        getline(cin, mood);
        cout << "Wake-up time: ";
        getline(cin, wakeUpTime);
        cout << "Sleep time: ";
        getline(cin, sleepTime);
        cout << "Work/Study hours (number): ";
        cin >> workHours;
        cin.ignore();
    }
};

// --- 4. Usage Tracking ---
class UsageTracking
{
protected:
    vector<string> favoritePlatforms;
    vector<string> dailyWebApps;

public:
    void inputUsageTracking()
    {
        int n, m;
        cout << "Number of favorite platforms: ";
        cin >> n;
        cin.ignore();
        for (int i = 0; i < n; ++i)
        {
            string plat;
            cout << "Platform " << i + 1 << ": ";
            getline(cin, plat);
            favoritePlatforms.push_back(plat);
        }
        cout << "Number of daily-used apps/websites: ";
        cin >> m;
        cin.ignore();
        for (int i = 0; i < m; ++i)
        {
            string app;
            cout << "App/Web " << i + 1 << ": ";
            getline(cin, app);
            dailyWebApps.push_back(app);
        }
    }
};

// --- 5. Blocker Settings (Inheritance & Vector Use) ---
class BlockerSettings : public UsageTracking
{
    // Inherits favoritePlatforms, dailyWebApps
    vector<string> blockList;
    int blockTime;
    int repeatUsageLimit;
    int platformSwitchFreq;

public:
    void inputBlockerSettings()
    {
        int k;
        cout << "Number of apps/webs to block: ";
        cin >> k;
        cin.ignore();
        for (int i = 0; i < k; ++i)
        {
            string item;
            cout << "To block: ";
            getline(cin, item);
            blockList.push_back(item);
        }
        cout << "Block time (in mins): ";
        cin >> blockTime;
        cout << "Repeat usage limit (days): ";
        cin >> repeatUsageLimit;
        cout << "Platform switch frequency (days): ";
        cin >> platformSwitchFreq;
        cin.ignore();
    }
};

// --- 6. Planning Setup ---
class PlanningSetup
{
    vector<string> timeTable;
    vector<pair<string, string>> subjectPlatformLinks;

public:
    void inputPlanningSetup()
    {
        int n;
        cout << "Subjects in timetable: ";
        cin >> n;
        cin.ignore();
        for (int i = 0; i < n; ++i)
        {
            string subject;
            cout << "Subject " << i + 1 << ": ";
            getline(cin, subject);
            timeTable.push_back(subject);
        }
        for (const string &subject : timeTable)
        {
            string link;
            cout << "Platform link for " << subject << ": ";
            getline(cin, link);
            subjectPlatformLinks.push_back(make_pair(subject, link));
        }
    }
};
};
};
