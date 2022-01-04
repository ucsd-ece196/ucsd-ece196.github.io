_Written by Dillon Hicks_


## Lists

Now that we have gone over some basics of Python syntax, let's go over something a bit more useful - **Lists**! They are most commonly used as arrays, as seen in languages such as C and Java, but can be used as so much more. Lists are an extremely useful data structure and can be used as **arrays, queues, stacks**. They can also **hold variables of different types**, which makes them very versatile. You can define them with **square brackets, with elements of that list separated by commas**.


For example, if we wanted to define a list, named `my_list`, with numbers 1-5, we can define it as such:
```python
my_list = [1,2,3,4,5]
```
Lists become even more powerful with the use of loops, as shown in the next section.

### List Indexing

You can access specific elements of Lists with **indexing**

You can get elements of a List with brackets after a list surrounding the index
Python has zero-indexed lists, which means the indexing starts from 0 like a normal language (*looking at you Matlab...*)

```python
# Using previous my_list variable
# Should print 1, the 0th element
print(my_list[0])
```

You can edit elements the same way, with list indexing. For example, if you wanted the first element of the previous `my_list` variable to be 0, you can simply do the following:

```python
# Using previous my_list variable
my_list[0] = 0

# Should print [0,2,3,4,5]
print(my_list)
```

!!! info

    You can also index lists in many other ways, for example **negative list indexing** and **slices**. This isn't *necessary* per se to use lists, but they are super useful, and will almost certainly be used if you want to properly do any coding technical interviews in Python (which is recommended due to the ease of python. For additional information, check out these resources on list slicing and advanced indexing.

    [Negative List Indexing](https://www.geeksforgeeks.org/python-negative-index-of-element-in-list/)

    [List Slices](https://www.geeksforgeeks.org/python-negative-index-of-element-in-list/)

### List Modification
In addition if you want to modify a list by making it larger, and not just changing elements, you can use `append()` and `extend()` to add values to the end of the list.

`append()` is used to add a single value to the end of a list.

```python

```

`append()` is used to add a single value to the end of a list.

```python

```

In order to remove an element from a list, you can use the `remove()` or `pop()` functions. `remove()` removes the first element with the value given, while `pop()` removes the last element or the element with the specified index

```python

```



### List Length

If you want the length of a list, you can use the `len()` function. This function can also be used to find the length of strings as well. 

```python
hands_on_classes = ["ECE 196", "ECE_5", "ECE 16", "ECE 115"]

# Should print 4, since there are 4 variables in the hands_on_classes variable
print(len(hands_on_classes))
```

### String Manipulation

Now that we have learned lists, we will quickly go over some of the operations you can do on strings. Strings operate a lot like lists or arrays, so These types of operations on strings are something that you see very often in natural language processing workflows for python, and more generally, whenever you want to parse text from a user or display text properly. 

There are many string manipulation methods, and we definitely won't talk about all of these here, but there are some useful operations that might be useful for your future python career and **cough cough** assignments for this class.

You can concatenate lists (put one list after another)  with the `+` symbol, similar to addition with Python standard arithmetic. 

```python
# Should print "HelloWorld" (We didn't put a space)
print("Hello" + "World")

# Should print "Hello World"
print("Hello " + "World")
```

We can also split these strings by certain characters with the [`split()`](https://www.geeksforgeeks.org/python-string-split/) function. Splitting a list by characters will . This is especially useful when you want to break up a sentence into a list of words, or character-separated values into those individual values. Similarly, you can use [`join()`](https://www.geeksforgeeks.org/python-string-join-method/)

```python
my_str = "Hello my name is"

# Should print ["Hello, "my", "name", "is"]
print(my_str.split())
```

In addition we can use some other functions to see whether a string represents an integer. 

```python
my_str = "Hello my name is"
my_str_2 = "123"

# Should print False
print(my_str.isdigit())

# Should print True
print(my_str_2.isdigit())
```

There are other similar functions that you can use such as [`isalpha()`](https://www.geeksforgeeks.org/python-string-isalpha-method/) and [`isdecimal()`](https://www.geeksforgeeks.org/python-string-isdecimal/)
## Loops

Now that we have gone over lists and strings, let's go over loops so we can establish a real-world usage for what we just learned. 

### While Loops 
While loops will continue repeating everything indented under it, as long as the expression evaluates to `True`. This has a similar behavior to while loops in other languages!

### For Loops

## [Problem 2] Short Questions

!!! question
    You are given 21 daily temperature readings from a remote device and are asked to do some data analysis on it. These values are given to directly to your python program. 

    1. Print whether the list 

    2. What functions might you use to find the minimum, maximum, and average temperatures of this list? (Google how to do this)

    3. 

    Given a list of temperatures, 

    Skeleton Code:
    ```python

    #Imagine that this list 
    temperatures = [68.21122500672686, 73.79972316786628, 66.7749840549457, 70.32700390306779, 72.82555562328548, 65.81532465482273, 69.28429355033545, 68.45502278511506, 68.40738731886807, 68.45665260662977, 70.64380857251861, 70.80989113857657, 72.46875233355938, 70.64159500472778, 70.69598489886532, 68.05456954711212, 65.76790308648873, 72.75473876512704, 69.43152327781354, 66.11085635300678, 67.15382574614719]

    # Print whether this list has length 21 or note, note that this list can change, so just use it's variable rather than printing true or false
    # YOUR CODE HERE

    # Print the minimum, maximum, and average temperatures
    # YOUR CODE HERE

    # Split the list into 3 weeks, and calculate the minimum, maximum, and average temperatures. 
    # YOUR CODE HERE
    ```








## Functions

##


## [Problem 3] Phone Number Verification

!!!question

    **Phone number verification**

    Write a function, `phone_test()`, to test if a given string phone number in the form #-###-###-####, or ###-###-#### is a valid phone number. For example, the phone number could be given could be in the form 1-858-534-2230 or 858-534-2230, abc-123-defg, with the last example an invalid number. Note that all are separated by the `-` character. 

    Hint, use the `split` function to split the initial string, then loop through that list to verify that each is valid and there are a proper amount of splits.

    Skeleton code (copy and paste the below into your .py file):

    ```python
    def phone_test(number):
        #WRITE YOUR CODE UNDER HERE


    #TEST CASES, DO NOT EDIT UNDER THIS LINE
    ```


