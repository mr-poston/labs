#include <iostream>

using namespace std;

int main()
{
    int num;
    string phrase;
    /* When we use cin >> to stream an input, it only takes the
     * next token, which is to say, the next part of the line. In
     * this case, it will take the next number, but leave the remainder
     * of the line. The only thing remaining may be a carriage return/enter,
     * but it still remains.
     * The getline below will read that carriage return/enter in and never
     * wait for the next prompt. To avoid this, we can use cin.ignore()
     * to clear out the remainder of the line.
     */
     cout << "Please pick a number from 1 to 10: ";
     cin >> num;

     /* Run this first with the cin.ignore() commented out. Then uncomment
      * and run again.
      */

      // cin.ignore();

      cout << "Now type a phrase: ";
      /* getline reads up to the next <enter>, so we need to make sure
       * we clear the enter from the previous prompt using cin.ignore()
       */
       getline(cin, phrase);

       cout << "Your number is " << num << endl;
       cout << "Your phrase is " << phrase << endl;

       return 0;
}
