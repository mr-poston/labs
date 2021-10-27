/* Multi-line comments start and end with slash star
   and star slash*/
// Single line comments use two slashes

/*
 * At the top of our program, we use include statements to
 * add libraries to our code. Libraries from the Standard (std) library
 * are added with the name between < and >.
 */
#include <iostream>

// After import statments, we can define the namespace we are using
using namespace std;

/*
 * C++ is mainly an Object Oriented language, but does still have some
 * characteristics of a structured language. We will see more of this
 * later, but notice we can define things outside of any function.
 * It is also important to note that C++ reads the program from the
 * top down and things like functions must be defined before they are
 * called.
 */

string dayOfWeek = "Saturday";

/*
 * Every program starts execution at the main function. This function
 * always returns and integer and by convention, we return 0 to signify
 * a normal termination of the program. We really won't be using this,
 * but it needs to be included.
 */

int main()
{
    cout << "Hello!" << endl;
    cout << dayOfWeek << " is my favorite day of the week." << endl;

    return 0;
}
