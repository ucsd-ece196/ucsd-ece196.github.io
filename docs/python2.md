_Written by Dillon Hicks_


## Lists

<iframe width="2736" height="807" src="https://www.youtube.com/embed/LcvSstN35Yo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Now that we have gone over some basics of Python syntax, let's go over something a bit more useful - **Lists**! They are most commonly used as arrays, as seen in languages such as C and Java, but can be used as so much more. Lists are an extremely useful data structure and can be used as **arrays, queues, stacks**. They can also **hold variables of different types**, which makes them very versatile. You can define them with **square brackets, with elements of that list separated by commas**.


For example, if we wanted to define a list, named `my_list`, with numbers 1-5, we can define it as such:
```python
my_list = [1,2,3,4,5]
```
Lists become even more powerful with the use of loops, as shown in the next section.

### List Indexing

You can access specific elements of Lists with **indexing**

You can get **elements** of a List with brackets after a list variable surrounding the index
Python has **zero-indexed lists**, which means the indexing starts from 0 like a normal language (*looking at you Matlab...*)

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
For these examples, we will use a list of strings representing the classes in a student's schedule. 

In addition if you want to modify a list by making it larger, and not just changing elements, you can use `append()` and `extend()` to add values to the end of the list.

`append()` is used to add a single value to the end of a list. For example, if we want to add `"ECE 143"` as a class to our list represening our list of classes, we can simply do

```python
class_list = ["ECE 196", "ECE 111", "ECE 225A"]
class_list.append("ECE 143")

#class_list now should be ["ECE 196", "ECE 111", "ECE 225A", "ECE 143"]
print(class_list)
```

`extend()` is used to add a the valus of a list in order to the end of another list. You can use this when you want to add multiple values to the end of a list with one statement. Note, if we try to append a list to the end of a new list, we get the original list as a **single** element in the new list. With the example below, if we want to add 2 classes to the list of classes, we get this list within a list, which is a bit weird. 

```python

class_list = ["ECE 196", "ECE 111", "ECE 225A"]
class_list.append(["ECE 143","ECE 175A"])

#class_list now should be ["ECE 196", "ECE 111", "ECE 225A", ["ECE 143", "ECE 175A"]]
print(class_list)


```

In order to get all of these elements in the original list, we can use `extend()`. This results in our list having the new classes added as expected, with the new 2 classes being added as 2 more elements in our list of classes. 

```python

class_list = ["ECE 196", "ECE 111", "ECE 225A"]
class_list.extend(["ECE 143","175A"])

#class_list now should be ["ECE 196", "ECE 111", "ECE 225A", "ECE 143", "ECE 175A"]
print(class_list)


```

In order to remove an element from a list, you can use the `remove()` or `pop()` functions. `remove()` removes the first element with the value given, while `pop()` removes the last element or the element with the specified index and then returns that element. For example, if we wanted to drop a class, we can simply remove one of the elements using `remove()`, or `pop()`

With `remove()`, we can remove the first element with the value provided, or if we wanted to remove `"ECE 111"` from the list of classes, we can simply do:

```python
class_list = ["ECE 196", "ECE 111", "ECE 225A", "ECE 143", "ECE 175A"]

class_list.remove("ECE 111")
#class_list now should be ["ECE 196", "ECE 225A", "ECE 143", "ECE 175A"]
print(class_list)
```

With `pop()`, we can remove the element at the index provided, or the class at the index 1, or `ECE 111` in the list of classes:

```python
class_list = ["ECE 196", "ECE 111", "ECE 225A", "ECE 143", "ECE 175A"]

class_list.pop(1)
#class_list now should be ["ECE 196", "ECE 225A", "ECE 143", "ECE 175A"]
print(class_list)
```

We can alternatively use `pop()` to remove the last element in the list, in this case, it should be "ECE 175A"

```python
class_list = ["ECE 196", "ECE 111", "ECE 225A", "ECE 143", "ECE 175A"]

#class_list now should be ["ECE 196", "ECE 225A", "ECE 143"], also returns the element popped
print(class_list.pop())
```

### List Length

If you want the length of a list, you can use the `len()` function. This function can also be used to find the length of strings as well. 

```python
hands_on_classes = ["ECE 196", "ECE_5", "ECE 16", "ECE 115"]

# Should print 4, since there are 4 variables in the hands_on_classes variable
print(len(hands_on_classes))
```

### String Manipulation

<iframe width="2736" height="807" src="https://www.youtube.com/embed/pKDSmZc750o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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

<iframe width="2736" height="807" src="https://www.youtube.com/embed/_bY4-_HEVik" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### While Loops 
While loops will continue repeating everything indented under it, as long as the expression evaluates to `True`. This has a similar behavior to while loops in other languages!

For example, if we want to print `"Hello World"` *forever*, we can simply use the following:

```python
while True:
    print("Hello world")
```

You can use **CTRL-C** to exit this infinite loop and stop Python. 

It might be dumb to print this forever, but we promise that this type of infinite loop can be very useful! For example if your microcontroller has a function `read_sensor()`, which gets values from a sensor and puts them somewhere, and you want to do this forever (or as long as your device is on), you can use the while loop similarly to what we had before.

```python
while True:
    # Read
    read_sensor()
```

However, what if we want to read multiple sensors? Say you can plug in an integer value into the `read_sensor()` function to read a specific sensor indicated by a specific index. For example, to test the 2nd sensor, or the sensor at the 1st index, we could yse `read_sensor(1)`. So using a variable, `n_sensors` as the number of sensors, in order to read all the sensors, we can do the following. 

```python
n_sensors = 6
i = 0
# Iterates while i is less than 6
while i < n_sensors:
    # Reads the ith sensor
    read_sensor(i)
    i += 1
```

Alternatively, we can similarly use `while` loops to access the values in a list in order. We can use the counter, stored in the variable `i`, to see what index of the list we are currently printing. For example, if you had a list of sensor names, you can print the names of the sensors one at a time with:
```python
#If you are curious, check out what these sensors do!
sensor_names = ["DHT-11", "MPU-6050", "HC-SR04", "MQ-2"]
i = 0
# Iterates while i is less than the length of the sensor_names list
while i < len(sensor_names):
    # Prints the name of the ith sensor
    print(sensor_names[i])
    i += 1
```


!!! note

    The above uses Python **assignment operators**, please use the tutorial before for more steps on how to use them, they can be very useful in making your code be more concise!

    **[https://www.geeksforgeeks.org/assignment-operators-in-python/](https://www.geeksforgeeks.org/assignment-operators-in-python/)**

    In addition, For more ways to use While loops, for example the `break` and `continue` statement, which are prevalent in other coding languages, please check out this tutorial to find out more! 
    
    **[https://www.geeksforgeeks.org/python-while-loop/](https://www.geeksforgeeks.org/python-while-loop/) **

### For Loops

However, what if we wanted to iterate through the values in a more readable way? **This is what `for` loops are for.**

For loops in python act much like `foreach` statements in other languages. They can give you values in a collection, for example a list, in order. `for` loops are very versatile to get values from lists (and really any other value that you can iterate over), and should be used over while loops when iterating over collections of variables, such as a list. 

For example, we could do the previous example in a much more concise way, and not have to use counters (the `i` variable), to keep track of what index we are on. 

```python
sensor_names = ["DHT-11", "MPU-6050", "HC-SR04", "MQ-2"]
# Prints each sensor name, one by one
for name in sensor_names()
    print(name)
```

!!! caution

    On the other hand, you might be wondering (probably not), what if I wanted to count with in a `for` loop? This is fairly easy with python, **you can simply use the range() function. `range()`, when iterated over in a `for` loop, will yield integer values in order over the values specified by `range()`**. `range()` can be used as such:

    `range(stop)`

    `range(start, stop[, step])`

    For example, if you print the values in `range(5)` with a `for` loop, you will get the values 0 - 4.

    ```python
    for i in range(5):
        print(i)
    ```

    Additionally, we
    
    
    If you want to access the values from `range()` without iterating through it, you simply cant use the value returned from `range()`. You must cast this `range()` value to a list, and then access all of these values. 
    This is because `range()` is a generator in that it does not give all values at once, but generates these values as it is called by `for`, or any other method which can request the next value in range. 

    ```python
    # Does not work
    print(range(7))

    # Does work, you can see all values given by range
    print(list(range(7)))
    ```

    You can also use range similar to to slices as mentioned in a note earlier and using the step argument, please check out more advanced usage in this article: 

    [https://www.geeksforgeeks.org/python-range-function/](https://www.geeksforgeeks.org/python-range-function/)

    Learning how `range()` operates is not needed to get started coding in Python or this class, but learning what it does should be essential to your future Python career!


## [Problem 3] Temperature Data Analysis

!!! question
    You are given 21 daily temperature readings from a remote device and are asked to do some data analysis on it. These values are given to directly to your python program. 

    1. Print "Not a list of temperatures" if every value in the temperatures list is not a number (a float or int), or "This is a list of temperatures". How did you test whether this worked (what test temperature lists did you use to check whether the list did or did not contain non-numbers) 

    2. What functions might you use to find the minimum, maximum, and average temperatures of this list? (Google how to do this) Implement these functions in your code to find and print the minimum, maximum, and average temperatures of this list.

    3. You are told to split these temperatures into 3 weeks to find statistics for each of these weeks. Link a tutorial or a set of resources that might help you do this (split this list into chunks of 7). Then, calculate the statistics from #2 for each week and print these values.

    Skeleton Code:
    ```python
    #Imagine that this list is given somewhere else in the program 
    temperatures = [68.21122500672686, 73.79972316786628, 66.7749840549457, 70.32700390306779, 72.82555562328548, 65.81532465482273, 69.28429355033545, 68.45502278511506, 68.40738731886807, 68.45665260662977, 70.64380857251861, 70.80989113857657, 72.46875233355938, 70.64159500472778, 70.69598489886532, 68.05456954711212, 65.76790308648873, 72.75473876512704, 69.43152327781354, 66.11085635300678, 67.15382574614719]

    # Print whether this list contains only numbers
    # YOUR CODE HERE

    # Print the minimum, maximum, and average temperatures
    # YOUR CODE HERE

    # Split the list into 3 weeks, and calculate the minimum, maximum, and average temperatures. 
    # YOUR CODE HERE
    ```

## Functions

If you have used a different coding language before, you may be very familiar with functions! If you haven't you'd be happy to know that you have been using function this entire time! For example, `print()` is a function that takes a variable and outputs its string representation to `stdout`, `type()` returns the type of a variable, and `isdigit()` is a class method of the string class that returns `True` for variables that represent a digit. You would also be happy to know that creating a function, or a set of self contained python code that can run a certain task, is very easy! 

You can think of functions as their relation to mathematics, in that a function takes in an input, and gives an output. For example, we can set $f(x)$ as a function

We can implement functions in Python using the `def` keyword.

```python
def f():
    print("Process within a function")
```

Creating a function without an output has its uses, for example if we want to run a process without having to repeat code. For example, this can be used to generalize a workflow such as starting up a microcontroller. 

```python
def start_up():
    check_voltage()
    test_sensors()
    #etc...
```

If we want to return something from this function, or get an output from it, we can use the `return` keyword as well. This is similar to many other languages such as C or Java.

```python
def sensor_count():
    sensor_names = ["DHT-11", "MPU-6050", "HC-SR04", "MQ-2"]
    return len(sensor_names)
```


However, this is not very useful in all cases, as this function will always have the same behavior every time it is run. This is like establishing the function $f(x)$ as

$$
f(x) = 2 + 2
$$

In order to change the behavior of these functions, functions can take in variables as arguments to be used when running a function.


```python
def check_voltage(voltage):
    if (voltage > 4) and (voltage < 6):
        print("Voltage is good") 
    else:
        print("Check voltage")

voltage = 4.5
check_voltage(voltage)
```






## [Problem 4] Phone Number Verification

!!!question

    **Phone number verification**


    You get a new job at a consumer electronics company who was contracted to make card scanners for brick-and-mortar stores. This company hired you because of your impressive Python skills that you acquired as a result of ECE 196. Your first task as an engineer at this company is to write a script to verify whether the numbers entered by customers into the new device, which has a full keyboard, are valid. 

    <center>
    <img src="/img_python/phonething.jpg" alt="drawing" width="200"/>
    </center>


    Write a function, `phone_test()`, to test if a given string phone number in the form #-###-###-####, or ###-###-#### is a valid phone number. For example, the phone number could be given could be in the form 1-858-534-2230 or 858-534-2230, abc-123-defg, with the last example an invalid number. Note that all are separated by the `-` character. 

    Hint, use the `split` function to split the initial string, then loop through that list to verify that each is valid and there are a proper amount of splits.

    Skeleton code (copy and paste the below into your .py file):

    ```python
    def phone_test(number):
        #WRITE YOUR CODE UNDER HERE


    #TEST CASES, DO NOT EDIT UNDER THIS LINE
    ```


***And that's it for this set of the Python section of the class. In the next set, we will go over more advanced function usage, some more useful data structures, and classes.***