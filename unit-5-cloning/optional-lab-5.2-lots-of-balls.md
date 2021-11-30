# (Optional) Lab 5.2 - Lots of Balls

In this lab, you will use cloning to create many identical sprites without having to rescript each one individually.

### Part 1 - Follow the bouncing sprites

1. Create a script that contains a single sprite, choose from available costumes (i.e. basketballs, hearts, stars, balloons, Alonzo, doves). When `the green flag` is clicked, the sprite should go to the center of the stage, pick a random direction, and start moving in the chosen direction. If the sprite hits a wall, it should bounce off and keep moving.
2. Modify the script to be controlled by the stage rather than by the sprite itself. When the spacebar is pressed, the stage should broadcast a message that triggers the sprite's movement. Pressing the spacebar again should restart the sprite's movement, including a new speed and new direction.
3. What would you need to do to add a second bouncing sprite (that behaved in the same way) to the script? What about 10 sprites? 100 sprites? What would happen if you wanted to change the speed of all the bouncing sprites in the script after you had created 100?

### Part 2 - Clones

1.  Modify your script so that, instead of a single sprite restarting each time the spacebar is pressed, a new clone of that sprite is created. You'll want to use the **Create a Clone of** and **When I starts as a clone** blocks in place of **Broadcast block** and **When I Receive** block.

    [![Create a Clone of](https://github.com/TEALSK12/introduction-to-computer-science/raw/master/images/create\_a\_clone\_of.png)](https://github.com/TEALSK12/introduction-to-computer-science/blob/master/images/create\_a\_clone\_of.png)

    [![When I starts as a clone](https://github.com/TEALSK12/introduction-to-computer-science/raw/master/images/when\_i\_start\_as\_a\_clone.png)](https://github.com/TEALSK12/introduction-to-computer-science/blob/master/images/when\_i\_start\_as\_a\_clone.png)

    [![Broadcast block](https://github.com/TEALSK12/introduction-to-computer-science/raw/master/images/broadcast.png)](https://github.com/TEALSK12/introduction-to-computer-science/blob/master/images/broadcast.png)

    [![When I Receive block](https://github.com/TEALSK12/introduction-to-computer-science/raw/master/images/when\_i\_receive.png)](https://github.com/TEALSK12/introduction-to-computer-science/blob/master/images/when\_i\_receive.png).
2. What happens to the original ("master") sprite each time the spacebar is pressed? Does that seem useful? What role should the original sprite play now that we're cloning?
3. Modify the script so that the original ("master") sprite hides at the beginning of the script and each new sprite appears when it is created.
4. Save your project as _Lab5.2_.

Bonus: Assign each clone a different value for some properties, such as speed, color, or size. Try controlling these values from the master sprite rather than having each clone choose its own.

### Grading rubric

| 1.1 One bouncing sprite                  | 1 point      |
| ---------------------------------------- | ------------ |
| 1.2 Sprite controlled by stage           | 1 point      |
| 2.1 Clones created by stage              | 1 point      |
| 2.3 Hide master sprite                   | 1 point      |
| Bonus: Sprites have different properties | 1 point      |
| **PROJECT TOTAL**                        | **5 points** |
