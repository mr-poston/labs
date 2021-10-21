# Other

For this project, you will implement a side-scrolling platform game (similar to Super Mario Bros.)

## Overview

Platform games are among the most widely recognized types of video games. Composing about one third of all console games at the peak of their popularity, platform games are characterized by their relative simplicity and by the common gameplay element of jumping across suspended platforms (hence the name) to avoid falling into a hazard. Platform games also typically include enemy characters, items that grant the hero special abilities ("power-ups"), and a "checkpoint" system that allows the player to restart from partway through a game or level when he or she dies.

### Example Side-Scrolling Platform Game

N.B. The example in the video below was NOT created using Snap!, but you _could _create something similar!

{% embed url="https://youtu.be/xQb3w182s7I" %}
Example of a side-scrolling platform game
{% endembed %}

## Details

### Controllable Sprite (aka "Hero")

Your script should have a "Hero" sprite. For example, Mario is the Hero in Super Mario Bros. The Hero should respond to user input. Specifically:

* Hero should clearly "face" right when you push the right arrow key.
* Hero should clearly "face" left when you push the left arrow key.
* Hero should perform an animated "in-place" walk when you hold the left or right arrow key.
* Hero should jump based on some input (you can decide the key or mouse click).

### Moving Scenery Sprites

You should have scenery sprites that move based upon Hero's traveling on the level. It is up to you to decide the level scenery, but you should meet the following requirements:

* There should be at least two scenery sprites (for example, a mountain and a tree).
* You should layer these sprites relative to Hero and each other. For example, Hero should always be "in front" of any background scenery sprites.
* Scenery sprites move relative to Hero as s/he moves. For example, when you hold down the right arrow key, the background sprites should move from right to left across the stage.
* Following with the layers, scenery sprites should move at different speeds so that one seems farther away. For example, a faraway mountain should move more slowly than a nearby tree.
* Scenery sprites should roll-over / re-appear when they hit the edge of the stage. For example, when Hero is walking to the right, the scenery sprites should re-appear on the right side of the stage when they roll off the left.

### On-Ground Enemy

There should be an on-ground enemy for Hero to contend with. Specific criteria include:

* There is at least on on-ground enemy.
* The enemy sprite moves towards Hero, independent of whether Hero is moving (i.e., regardless of whether the user is pressing an arrow key).
* The enemy sprite re-appears / rolls-over when s/he hits the edge of the stage.
* The enemy sprite is animated when he is moving towards Hero.
* If Hero does not jump, s/he runs into the enemy and the game ends with an appropriate message. **Hint:** you can use the `stop all` block to end all scripts.
* It should be possible for Hero to jump over the enemy.

## Programming Habits

You will be required to incorporate good programming habits in your script:

* Use Start and Stop blocks.
* Make sure you initialize state appropriately so that your script is repeatable.
* Add comments to your script so it is easy to understand.
* Keep your scripting area organized and clear of all unnecessary blocks. (If you don't need the block, delete it!)
* Use custom blocks to break the script down into logical parts.

## Additional Extensions

Once you complete the requirements above, you can extend your script. Some suggestions:

* Include flying enemies for Hero to dodge or duck.
* Keep score based on how many objects Hero gets by. **Hint:** Use a variable and show it on the screen.
* Have Hero jump to 'grab' an object that offers Hero extra points or more powerful abilities (such as jumping higher or not being killed when s/he runs into an enemy). The objects must appear at random times and move smoothly as Hero runs.

## Grading Rubric

The detailed list for how your project will be graded is below. Please review your project before submitting to be sure you meet all of the requirements! If you have any questions on whether you've met a requirement, ask Mr. Poston!!

| Requirement                                                                                                                                                                           | Points                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Hero turns to the right on right arrow key                                                                                                                                            | 5                                                |
| Hero turns to the left on left arrow key                                                                                                                                              | 5                                                |
| Hero performs an in-place animated walk if you hold down either arrow key                                                                                                             | 5                                                |
| Hero jumps based on some input                                                                                                                                                        | 5                                                |
| There are at least two scenery sprites                                                                                                                                                | 5                                                |
| Scenery sprites are layered with Hero (i.e., appropriate layering blocks are in your script)                                                                                          | 5                                                |
| Scenery sprites move based on Hero's movement                                                                                                                                         | 5                                                |
| Scenery sprites move at different speeds (e.g., far away versus near)                                                                                                                 | 5                                                |
| Scenery sprites roll-over when they fall off the stage                                                                                                                                | 5                                                |
| There is at least one on-ground enemy                                                                                                                                                 | 5                                                |
| Enemy sprite always moves toward Hero                                                                                                                                                 | 5                                                |
| Enemy sprite re-appears / rolls-over correctly                                                                                                                                        | 5                                                |
| Enemy sprite is animated when it moves                                                                                                                                                | 5                                                |
| If Hero does not jump, s/he runs into the enemy and the game ends nicely and properly                                                                                                 | 10                                               |
| Hero can jump over the enemy                                                                                                                                                          | 5                                                |
| _Good programming #1:_ script has clear start and stop                                                                                                                                | 5                                                |
| _Good programming #2:_ script is repeatable and initializes state correctly                                                                                                           | 5                                                |
| _Good programming #3:_ use of comments in your script                                                                                                                                 | 5                                                |
| _Good programming #4:_ scripting area is organized and clear of unnecessary blocks                                                                                                    | 5                                                |
| _Good programming #5:_ Custom blocks used to break down script into logical parts                                                                                                     | 5                                                |
| **Extra Credit:** Include flying enemies for Hero to dodge or duck                                                                                                                    | 5                                                |
| **Extra Credit:** Keep score based on how many objects Hero gets by                                                                                                                   | 5                                                |
| **Extra Credit: **Have Hero jump to 'grab' an object that offers Hero extra points or more powerful abilities. The objects must appear at random times and move smoothly as Hero runs | 10                                               |
| **Extra Credit:** Create your own extension                                                                                                                                           | 0-10                                             |
| **Total Points**                                                                                                                                                                      | **105** (135 possible with all the extra credit) |
