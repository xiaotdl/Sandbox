#include <iostream>
#include <ctime>

using namespace std;


int main()
{ 
/* == C++ Date and Time ==
 * There are 4 time-related types:
 * clock_t, time_t, size_t, tm
 */
/*
 * struct tm {
 *   int tm_sec;   // seconds of minutes from 0 to 61
 *   int tm_min;   // minutes of hour from 0 to 59
 *   int tm_hour;  // hours of day from 0 to 24
 *   int tm_mday;  // day of month from 1 to 31
 *   int tm_mon;   // month of year from 0 to 11
 *   int tm_year;  // year since 1900
 *   int tm_wday;  // days since sunday
 *   int tm_yday;  // days since January 1st
 *   int tm_isdst; // hours of daylight savings time
 * }
 */
    // current date/time based on current system
    time_t now = time(0);

    // convert now to string form
    char* dt = ctime(&now);

    cout << "The local date and time is: " << dt << endl;

    // convert now to tm struct for UTC
    tm *gmtm = gmtime(&now);
    dt = asctime(gmtm);
    cout << "The UTC date and time is:" << dt << endl;


/* Format time using struct tm */
    cout << "Number os sec since January 1, 1970: " << now << endl;

    tm *ltm = localtime(&now);

    // print various components of tm structure.
    cout << "Year: "<< 1900 + ltm->tm_year << endl;
    cout << "Month: "<< 1 + ltm->tm_mon<< endl;
    cout << "Day: "<<  ltm->tm_mday << endl;
    cout << "Time: "<< 1 + ltm->tm_hour << ":";
    cout << 1 + ltm->tm_min << ":";
    cout << 1 + ltm->tm_sec << endl;

/* == C++ Basic Input/Output ==
 * I/O Library Header Files
 * <iostream>: defines cin, cout, cerr, clog objects.
 * <iomanip> : declares services useful for performing formatted I/O, e.g. setw, set precision
 * <fstream> : declares services for user-controlled file process
 */
    // cout
    char str[] = "Hello C++";

    cout << str << endl;

    // cin
    char name[50];

    cout << "Please enter your name: ";
    cin >> name;
    cout << "Your name is: " << name << endl;

    // cerr
    char str_[] = "Unable to read...";

    cerr << "Error message : " << str_ << endl;

    // clog 
    char str_1[] = "Unable to read...";

    clog << "Error message : " << str_1 << endl;

    return 0;
}
