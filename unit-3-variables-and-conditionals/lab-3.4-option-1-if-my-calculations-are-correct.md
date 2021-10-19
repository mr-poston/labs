# Lab 3.4 (Option 1) - If My Calculations are Correct

In this lab, you will write custom **reporter** and **predicate** blocks to perform several useful calculations and computations.

### Simple Computations

1.  Write a custom **reporter** block called **min** that determines which of two numbers is smaller and reports that value. If the two numbers are equal, report either one.

    Example: ![](../.gitbook/assets/min.png)should report **2**
2.  Write a custom **reporter** block called **max** that determines which of two numbers is larger and reports that value. If the two numbers are equal, report either one.

    Example: ![](../.gitbook/assets/max.png)should report **4**
3.  Write a custom **predicate** block called **between** that determines if a number is between two other numbers. If the first number is equal to either of the other two numbers or is between them, the block should report "true".

    Example: ![](../.gitbook/assets/between.png)should report **true**, because 4 is between 3 and 10
4.  Write a custom **predicate** called **\_ has at least \_ letters** that determines whether a word has at least a specified number of letters.

    Example: ![](../.gitbook/assets/long.PNG)should report **true**, because _hello_ has at least 5 letters
5. Save your project as _Lab3.4_.

### Challenge: Stepping Things Up

Write a custom **reporter** block called **distance to** that computes and reports the distance from a sprite's position to another point. Use the **x position** and **y position** blocks to determine the sprite's position. Remember that the formula for the distance between points `(x1, y1)` and `(x2, y2)` is `sqrt((y2-y1)^2+(x2-x1)^2)`.

Example: if your sprite is at (1,0), ![](<../.gitbook/assets/distance to.png>)should report **5**.

### Grading Scheme / Rubric

| Criteria                      | Points       |
| ----------------------------- | ------------ |
| 1.1 min                       | 1 Point      |
| 1.2 max                       | 1 Point      |
| 1.3 between                   | 1 Point      |
| 1.4 has at least \_\_ letters | 1 Point      |
| Challenge                     | 1 Point      |
| **Total**                     | **5 Points** |
