#include <iostream>

using namespace std;

int main()
{
    // To read an entire line, you use the getline command.
    cout << "Please enter your full name: ";
    
    // Create a string variable and read in from the user
    string fullName;
    getline(cin, fullName);
    
    // You can stream multiple items to the output, like concatenating
    cout << "Hello " << fullName << "!" << endl;
    // endl tells C++ to move to a new line
    cout << "It is nice to meet you!" << endl;
    
    
    // To read a single word, you can use the cin command
    cout << "Please enter your first name: ";
    string name;
    cin >> name;
    
    cout << "Hello " << name << "!" << endl;
    cout << "It is nice to meet you!" << endl;
    
    return 0;
}
