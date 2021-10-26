As is customary in computer science, your first program is “Hello World!”

This example will simply print Hello World! to the console. Let’s take a closer look.

Including Libraries
The first line of your program specifies any additional libraries that you may want to use in the program.

C++ has a very limited set of commands automatically included, so it is typical to have several include statements.

Notice that the include statement does not have a semicolon after it. This is one of the few statements without a semicolon.

Standard Namespace
In the next part of your program you will find a namespace declaration. C++ allows users to override reserved command names, so anytime you use a command name, you need to tell it which version of the command to use. In other words, using the namespace of std provides scope to identifiers, such as types, commands, and functions.

To help simplify our program, you can use:

using namespace std;
This command tells C++ to use the command from the standard library if you don’t specify otherwise.

Main Function
Like other languages, C++ starts execution in the main function. In C++, the main function always returns an integer and by convention, you return a zero to signify a normal termination of the program.

Finally, Your Print Statement!
Finally, you see our print statement. In C++, you use cout, which is short for console output. This is then followed by angled brackets which show that Hello World! is being added to the console output stream.

Output to the Console
Any output you want to send to the console, you do with the cout output stream. You add to the stream using two angled brackets: <<

You can concatenate items by adding additional items to the stream with additional <<:

cout << "Hello " << name << ". It is nice to meet you!";
To go to a new line, you add either a \n inside the string or an endl command. In this course you will see the use of endl as our convention:

cout << "Hello" << endl;
cout << "World!" << endl;
