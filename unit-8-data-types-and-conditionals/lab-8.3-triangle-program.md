# Lab 8.3 - Triangle Program

## Part 1

Trace through the flow of execution for the following programs and predict what will happen for each one.

### Example 1

```python
a = input("What... is your quest? ")
b = "to seek the Holy Grail"
if a != b:
    print("Go on. Off you go.")
else:
    b = input("What...is the air-speed velocity of an unladen swallow? ")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHH [Bridgekeeper is thrown off bridge]")
    else:
        print("[You are thrown off the bridge]")
```

What would the output be if...

1. ... the user inputs `idk`?
2. ... the user inputs `to seek the Holy Grail`, then inputs `Huh`?

### Example 2

```python
user_input = input("What is your favorite color? ")
if user_input == 'blue':
    print("Blue Skidoo")
elif user_input == 'red':
    print("Roses are red!")
elif user_input == 'yellow':
    print("Mellow Yellow")
elif user_input == 'green':
    print("Green Machine")
elif user_input == 'orange':
    print("Orange you glad I didn't say banana?")
elif user_input == 'black':
    print("I see a red door and I want it painted black.")
elif user_input == 'purple':
    print("And we'll never be royalllssss")
elif user_input == 'pink':
    print("Pinky and the Brain")
else:
    print("I don't recognize that color. Is it even...??")
```

What would the output be if...

1. ... the user inputs `green`?
2. ... the user inputs `Red`?

## Part 2

In the editor (main.py), translate this Snap! program into a Python program!

![](../.gitbook/assets/triangle\_program.png)

#### Recreate the Triangle Program

* The program will ask for the lengths of all three sides of a triangle.
* The program will display what kind of triangle it is - or if it is even a triangle at all.
* The program will find the perimeter of the triangle.

## Bonus

Research lists in Python.

Re-implement Example 2 above using lists.
