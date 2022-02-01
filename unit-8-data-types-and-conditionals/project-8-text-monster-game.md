# Project 8 - Text Monster Game

## Game specifications

### Overview

This game takes place in a three-story virtual space. Each story (or floor) can have as many rooms as desired for game play. The player must navigate the levels in search of the prize. Along the way they collect items and fight monsters. On each move the player has seven possible commands: `left`, `right`, `up`, `down`, `grab`, `fight`. If the input is invalid (not one of these commands,) the game will let the player know. Otherwise, the game will execute the player's command. The goal of the game is to collect the prize guarded by the monster.

### Behavior Details

#### Behavior Example

```
What would you like to do? left
You see a sword.
What would you like to do? grab
You picked up the sword.
What would you like to do? left
You see nothing.
What would you like to do? left
You see a monster.
What would you like to do? fight
You defeated the monster!
What would you like to do? left
You see stairs going down.
What would you like to do? down
You see nothing.
```

**The game has three floors**

* Each floor is made up of at least five rooms, arranged in a line from left to right.
* A room can contain a sword, a monster, magic stones, up-stairs, down-stairs, a prize, or nothing.

**At the start of the game**

* The player should always start in the same room.

**Movement**

* The player can try to move to the left room or right room.
* If there is no room in that direction, the game should report this.
* The player can also move upstairs or downstairs if the room contains an up-staircase or a down-staircase.
  * The player can only go up if there is an up-staircase
  * The player can only go down if there is a down-staircase.
  * If a player uses a staircase, the room the player enters must contain a staircase in the opposite direction.
* The program should not allow the player to run past a monster.
* The program should not allow the player to go up, down, left, or right past the bounds of the game.

**Contents of rooms**

* The game prints out the contents of the current room after every command.
* The player can grab swords or magic stones if they walk into a room with them.
* The sword or stones are no longer in the room once grabbed.
* Your virtual world should have a minimum of 4 swords.
* Your virtual world must have a minimum of 1 magic stone.

**Monsters guard some rooms**

* The player can use a sword to defeat a monster using the fight command.
* The sword and monster disappear after fighting.
* If they have no sword, the player can exit in the direction from which they came.
* If the player fights without a sword, they will be defeated and the game will end.
* If they try to walk past a monster, they will be killed and the game will end.
* A sword _and_ magic stones are required to defeat a boss monster.

### Implementation Details

* The game should be implemented using lists.

**Player Items**

* Use a list to keep track of the player's items.
* At the beginning of the game it should be empty.
* Players can hold up to three items at a time.
* If a player attempts to pick up a fourth item, a warning message should be printed.
  * If a grab attempt fails, the item in question should remain in the room.

**Monsters**

* There should be three regular monsters placed throughout the game.
* Monsters require a sword to defeat.
* There should be a boss monster in the room just before the room that contains the prize.
* The boss monster requires magic stones _and_ a sword to defeat.

**Win/Lose**

* The game is won when the player grabs the prize.
* The game is lost if the player:
  * fights a monster without a sword.
  * fights the boss monster without a sword and stones.
  * tries to move past a monster.

## Checkpoints

To complete the lab successfully, divide up the coding task into a series of checkpoints. At each checkpoint, test all of the game features that have been implemented so far, to make sure that new code hasn't caused any bugs in features from previous checkpoints.

### Suggested Checkpoints

#### Checkpoint 0:

* Report current room contents correctly.
* Implement "help" command.

#### Checkpoint 1:

**Make "up", "down", "left", and "right" work correctly.**

* Do not need error checking.

#### Checkpoint 2:

**Add all error checks and messages related to movement.**

* It should _not_ be possible to:
  * move off the map
  * go up and down unless the right staircase is present

#### Checkpoint 3:

**Record the player's last movement direction.**

* If a room contains a monster, allow players to exit only in the direction from which they entered.
* Otherwise, print an appropriate "game over" message.

#### Checkpoint 4:

**Implement "grab" command.**

* Start by allowing unlimited inventory. Test for bugs. Then
  * Check inventory list length before starting "grab".
  * Print a refusal message if list is already length 3.
    * The item the player tried to grab should not be affected.
  * Monsters and stairs can never successfully be added to inventory.

#### Checkpoint 5:

**Implement "fight" command.**

* Check inventory for appropriate item(s) to defeat each monster / boss monster.
* Remove those items after successful fight.

#### Checkpoint 6:

**Decide what happens when the prize is picked up.**

* Go through each of the specs again and confirm that the code works correctly.

## Grading Rubric

### Functional Correctness (Behavior)

| Requirement                                                      | Points |
| ---------------------------------------------------------------- | ------ |
| Game has three floors                                            | 5      |
| User can move left or right, but not beyond the rooms            | 10     |
| User can only move up or down at an appropriate staircase        | 5      |
| Grab adds an item to the users collected items                   | 5      |
| User can only collect 3 items                                    | 2      |
| Help lists all possible commands                                 | 2      |
| Monsters either disappear if user has a sword or defeat the user | 5      |
| A sword can only be used once and then it disappears             | 6      |
| Boss monster needs sword and magic stones to be defeated         | 5      |
| Prize is blocked by boss monster                                 | 5      |
| **Sub total**                                                    | **50** |

### Technical Correctness

| Requirement                                                      | Points  |
| ---------------------------------------------------------------- | ------- |
| Correctly uses lists                                             | 15      |
| Correctly appends items to list of users collected items         | 15      |
| Correctly uses if statements to check items in user’s possession | 15      |
| Correctly using `or` statements and `and` statements             | 15      |
| **Sub total**                                                    | **60**  |
| **Total**                                                        | **110** |

## Extra Credit

* Add an 'inventory' command to display the items (if any) that the player is currently carrying.
* Implement Cardinal Directions into your code to give more control over direction for the player.
* Include a short description of each room, printed each time a player enters it -- and optionally a longer description of the same room, printed only the first time the player enters.
* **Advanced:** Randomly generate locations of monsters, magic stones and swords. Simple random placement is likely to make the game unplayable, so this will probably require a larger floor plan and careful design of the randomization.
