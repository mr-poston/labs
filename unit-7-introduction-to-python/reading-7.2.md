# Reading 7.2

## Values and Types

A value is one of the basic things a program works with, like a letter or a number. The values we have seen so far are 1, 2, and 'Hello, World!'.

These values belong to different types: 2 is an integer, and 'Hello, World!' is a string, so-called because it contains a “string” of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.

If you are not sure what type a value has, the interpreter can tell you.

```python
>>> type('Hello, World!')
<type 'str'="">

>>> type(17)
<type 'int'="">
```

Not surprisingly, strings belong to the type `str` and integers belong to the type `int`. Less obviously, numbers with a decimal point belong to a type called `float`, because these numbers are represented in a format called floating-point.

```python
>>> type(3.2)
<type 'float'="">
```

What about values like '17' and '3.2'? They look like numbers, but they are in quotation marks like strings.

```python
>>> type('17')
<type 'str'="">
>>> type('3.2')
<type 'str'="">
```

They’re strings.

When you type a large integer, you might be tempted to use commas between groups of three digits, as in 1,000,000. This is not a legal integer in Python, but it is legal:

```python
>>> 1,000,000
(1, 0, 0)
```

Well, that’s not what we expected at all!

Python interprets 1,000,000 as a comma-separated sequence of integers. This is the first example we have seen of a semantic error: the code runs without producing an error message, but it doesn’t do the “right” thing.

## Operators and Operands

Operators are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called operands.

The operators `+`, `-`, `*`_, `/`, `//`,_ and `**` perform addition, subtraction, multiplication, true division, floor division, and exponentiation, as in the following examples:

```python
20+32   hour-1   hour*60+minute   minute/60   minute//60   5**2   (5+9)*(15-7)
```

Python 3 has two division operators. The `/` operator, also known as _true division_, will always produce a floating point answer. The `//` operator, also known as _floor division_, will round the quotient down to the nearest integer:

```python
minute=170
>>> minute / 60
2.8333333333333335
>>> minute // 60
2
```

## Expressions and Statements

An expression is a combination of values, variables, and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions (assuming that the variable x has been assigned a value):

```python
17
x
x + 17
```

A statement is a unit of code that the Python interpreter can execute. We have seen two kinds of statement: print and assignment. Technically an expression is also a statement, but it is probably simpler to think of them as different things. The important difference is that an expression has a value; a statement does not.
