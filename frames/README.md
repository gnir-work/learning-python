## Function overloading
Have you ever written in java? or C? or basically any strictly typed language?  
How fun is it that you can write the following code, and the language just knows which function to call?

```c 
int print(char character) {
    // Do stuff related to printing a char
}

int print(char *characters) {
    // Do stuff related to printing an array of character
}
```

How fun will it be to add this functionality to all the cool stuff that python knows how to do?  
I think you got the basic idea :)
Please implement method overloading in python.

## Requirements
Make the following code valid

```python
from cool_features import overload

@overload
def print(character: int):
    # Handle printing a character represetned as a number

@overload
def print(characters: str):
    # Handle printing a string of characters

```

## Help
1. Read about decorators in python
2. Read about type annotations.
3. Try exploring the function object.

## Extra credit
Try implementing the same thing for class methods.
