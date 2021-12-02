# Cloning Sprites



**Discussion**

Think about how we create all the “invaders”?

* _**Answer with current knowledge:**_ make one invader sprite, and copy it many times while adjusting the copies as necessary.

What might go wrong or be bad about this approach?

* If anything in an invader changes, it will need to be changed many times.
* Lots of sprites clogging up the program that are all basically doing the same thing.

**Introduction to Cloning**

Cloning is the automated way of doing the manual copying

You can create a clone using:

[![Create a Clone of Block](https://github.com/TEALSK12/introduction-to-computer-science/raw/master/images/create\_a\_clone\_of.png)](https://github.com/TEALSK12/introduction-to-computer-science/blob/master/images/create\_a\_clone\_of.png)

Note that clones inherit all aspects of the "master" or "prototype" sprite, including scripts.

It is important to use the **When I start as a clone** block to ensure clones don't duplicate out of control.

[![When I start as a clone Block](https://github.com/TEALSK12/introduction-to-computer-science/raw/master/images/when\_i\_start\_as\_a\_clone.png)](https://github.com/TEALSK12/introduction-to-computer-science/blob/master/images/when\_i\_start\_as\_a\_clone.png)

#### Activity

Complete the Lots of balls lab (next page).

* This lab will be repeating much of what was in the lesson. This is intentional.
* Students should focus on ensuring they are differentiating between "master" sprites and "clone" sprites, and that the stage is serving as the main "driver" for the program.
