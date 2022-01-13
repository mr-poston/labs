# Project 7 - Mad Libs



Using Python, you will use variables, input, and printing to create a Mad Lib. You will also practice _designing_ a project by planning out your Mad Lib before implementing it. Part of the project is to use your creativity to design your own unique story.

### Overview

Mad Libs are a fun way to tell a story. The story is pre-written except for a few missing words. The story is hidden from the user. The user is asked a series of questions in order to fill in the missing words before seeing the story. Then the story is read off with the user's words mixed in!

### Details

#### Behavior

*   The program will print out the title of the Mad Libs story, as well as a short explanation of game play

    ```
    A Day in NYC: a Mad Lib.
    Welcome! You are about to play a fantastic word game.
    I will ask you for nouns, verbs, adjectives, proper nouns and adverbs.
    Using those words I will create an unexpected story for you!
    ```
*   The program should then prompt the user to enter in nouns, verbs, adjectives, proper nouns, and adverbs

    ```
    Enter a proper noun: Sally
    Enter a place in New York City: Times Square
    Enter another place in New York City: The Empire State Building
    Enter an adverb: quickly
    Enter a noun: donut
    Enter an adjective: slimy
    Enter a verb: prance
    Enter an adjective: beautiful
    ```
*   After all the words have been entered. The program will print out the story. You will need to create a story of your own choosing. Keep it clean and fun. Here is an example of a day in New York City.

    ```
    It was a beautiful day in New York City.
    Our hero, Sally, was on a walk from Times Square to The Empire State
    Building. Sally pranced rather quickly because he/she lived in
    beautiful New York for only a few months.
    Suddenly a slimy donut appeared out of nowhere!!!
    ```

#### Implementation Details

_**Plan out your story on pencil and paper first, before you start implementing the program.**_

1. Create your story
2. Select the missing words
3. Determine each words part of speech
4. Create introduction
5. Create questions
6. Divide story into print statements

As mentioned above the program must request words from the user. The following **must** be included in the program:

* 10 different words inputted
* Variable names should correspond to the part of speech requested and part of the story they belong to (e.g. `first_noun`, `second_verb`, etc.)
* Variable names should follow Python naming conventions:
  * use all lowercase letters
  * if the variable name is more than one word, use an underscore \_ to separate words. _Remember, variable names cannot contain spaces!_
* Comments should be used to aid in code readability.
