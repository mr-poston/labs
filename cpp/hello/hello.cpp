// Add the IO Stream library
#include <iostream>

/* Defining the namespace helps simplify our code
 * Using the std namespace means you do not have to
 * preface statements from the std library with std::
 */
using namespace std;

/* C++ starts by executing the main program. Each program must
 * contain a main function that returns an int value.
 */
int main()
{
    // cout stands for console output - our basic output statement
    cout << "Hello World!";
    
    /* Without the namespace declaration, the cout line would look
     like this:
     
     std::cout << "Hello World!";
    */
    
    // By convention, we return 0 to signify the program has finished
    // without error.
    return 0;
}
