# PYTHON VARIABLES
Variables are containers for storing data values.

## Creating Variables
Python has no command for declaring variable.
A variable is created the moment you first assign a value to it.
### Example:
```python
x = 5
y = 'John'
print(x)
print(y)
```
Variables do not need to be declared with any particular type, and can even change type after they have been set.
### Example:
```python
x = 4   # x is of type int
x = 'Sally'   # x is now of type str
print(x)
```

## Casting:
If you want to specify the data type of a variable, this can be done with casting.
### Example:
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

## Get The Type
You can get the data type of a variable with the type() function.
## Example:
```python
x = 5
y = 'John'
print(type(x))
print(type(y))
```

## Single or Double Quotes?
String variables can be declared either by using single or double quotes.
### Example:
```python
x = 'John'
# is the same as
x = "John"
```

## Case-Sensitive
variable names are case-sensitive.
### Example:
```python
a = 4
A = 'Sally'
# A will not overwrite a
```

## Variable Names
A variable can have a short name (like x and y) or a more descriptive name (e.g., age, carname, total_volume).
### Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain aplha-numeric characters and underscore(A-z, 0-9, and _)
- Variable names are case-sensitive (age, Age and AGE are different variables)
- A variable name cannot be any of the Python keywords(e.g., and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield).