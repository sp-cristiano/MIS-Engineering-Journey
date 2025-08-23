# PYTHON SYNTAX

As we learned in the previous page, Python can be executed by writing directly in the command line or by creating a python file on the server, using the `.py` file extension, and running it in the command line.

## Python Indentaion:

Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

### Example:

```python
if 5 > 2:
  print('Five is greater than two!')

```

Python will give you an error if you skip the indentation:

### Example:

Syntax Error:

```python
if 5 > 2:
print('Five is greater than two!')
```

The number of spaces is up to you as a programmer, the most common uses is four, but it has to be at least one and consistent through out the same block.

### Example:

```python
if 5 > 2:
  print('Five is greater than two!')
if 5 > 2:
        print('Five is greater than two!')
```

### Example:

Syntax Error:

```python
if 5 > 2:
  print('Five is greater than two!')
          print('Five is greater than two!')

```

## Python Variables:
In Python, variables are created when assign a value to it:
### Example:
```python
x = 5
y = 'Hello, World!'
```
Python has no command for declaring a variable.

## Comments:
Python has commenting capability for the purpose of in-code documentation.
Comments starts with a `#`, and Python will render the rest of the line as a comment.
### Example:
```python
# This is a comment.
print('Hello, World!')
```

