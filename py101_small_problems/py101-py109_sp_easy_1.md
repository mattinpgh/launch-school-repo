# PY 101 - PY 109
## Small Problems
### Easy 1

## Isn't it Odd?

Write a function that takes one integer argument and returns `True` when the number's absolute value is odd, `False` otherwise.


```python
def is_odd(num):
    return True if abs(num) % 2 != 0 else False
```

### Isn't it Odd? Recommended Solution
This is a little cleaner and shorter than my solution.
```
def is_odd(number):
    return abs(number) % 2 == 1
```

## Odd Numbers
Print all odd numbers from `1` to `99`, inclusive, with each number on a separate line.

**Bonus question**: Can you solve the problem by iterating over just the odd numbers?

_________________________

P: The problem seems pretty straightforward. Print (don't return) odd numbers (numbers not divisible by two) between and including 1 and 99, with each number in a new, separate line. The bonus queston asks to solve the problem by just iterating over the odd numbers, which prevents brute forcing a loop and doing modulus division on everything.

E: No examples or test cases are provided

D: I'm not sure that identifying a data structure is relevant. I could produce a list and print from the list, but this is a short, simple function and I don't think that's necessary. A range is a data structure.

A: Ok, the simplest way to solve this is with modulus division by two, printing out everything that doesn't have a result of 0 on a new line, but the bonus questin throws that out. The way to iterate over only the odd numbers would be a slice, starting at 1 and finishing at 100 with a step of 2. I don't want to type all the numbers in and I can't iterate through the odd numbers, so a range seems like the right way to do this. 

Initialize a range, slice the range in a loop, print the sliced range one by one



```python
my_range = range(100)
for num in my_range[1:100:2]:
    print(num)
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    23
    25
    27
    29
    31
    33
    35
    37
    39
    41
    43
    45
    47
    49
    51
    53
    55
    57
    59
    61
    63
    65
    67
    69
    71
    73
    75
    77
    79
    81
    83
    85
    87
    89
    91
    93
    95
    97
    99


### Odd Numbers Recommended Solution
I didn't actually know that you could add the step option to range() in a loop like that. I'll remember that.
```
for number in range(1, 100, 2):
    print(number)
```

## Even Numbers
Print all even numbers from `1` to `99`, inclusive, with each number on a separate line.

**Bonus question**: Can you solve the problem by iterating over just the even numbers?

_________________________

P: This seems pretty similar to the last problem. I'd say refer to those notes.

E: No examples or test cases are provided

D: I'm not sure that identifying a data structure is relevant. I could produce a list and print from the list, but this is a short, simple function and I don't think that's necessary. A range is a data structure.

A: Ok, the simplest way to solve this is with modulus division by two, printing out everything that has a result of 0 on a new line, but the bonus question throws that out. The way to iterate over only the odd numbers would be a slice, starting at 2 and finishing at 100 with a step of 2. I don't want to type all the numbers in and I can't iterate through the odd numbers, so a range seems like the right way to do this. 

Initialize a range, slice the range in a loop, print the sliced range one by one


```python
for num in range(2,100,2):
    print(num)
```

    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    22
    24
    26
    28
    30
    32
    34
    36
    38
    40
    42
    44
    46
    48
    50
    52
    54
    56
    58
    60
    62
    64
    66
    68
    70
    72
    74
    76
    78
    80
    82
    84
    86
    88
    90
    92
    94
    96
    98


### Even Numbers Recommended Solution

My solution is the same as the recommended solution.

## How Big is the Room?

Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet

_______________________________

P: Ok, the problem wants user input of two variables, length and width in meters. It prints (not returns) the room's areas (lw) in square meters and square feet. We'll have to get both variables, get the area in square meters, then get the converted area, then print.

E: There are no test cases

D: I think I'm just printing strings here

A: Input for two variables. \[skip data validation because of the scope.] create and assign area_in_metric = l*w. Create and assign area_in_imperial = area_in_metric * 10.7639. Print each in a single f-string.



```python
length = float(input('Enter the length of the room in meters: '))
width = float(input('Enter the width of the room in meters: '))
print(str(length * width) + " in square meters, or " + str((length * width) * 10.7639) + " in square feet")
```

    Enter the length of the room in meters:  9
    Enter the width of the room in meters:  6


    54.0 in square meters, or 581.2506 in square feet


### Further Exploration

Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.


```python
#l_temp = input('Enter the length of the room and \'m\' for meters, \'f\' for feet: ')
length, l_measurement = (input('Enter the length of the room and \'m\' for meters, \'f\' for feet. No comma, only two characters: ')).split()
width, w_measurement = (input('Enter the width of the room and \'m\' for meters, \'f\' for feet. No comma, only two characters: ')).split()

length = float(length)
width = float(width)

if l_measurement == "f":
    length /= 3.28084
if w_measurement == "f":
    length /= 3.28084

print(str(length * width) + " in square meters, or " + str((length * width) * 10.7639) + " in square feet")
```

    Enter the length of the room and 'm' for meters, 'f' for feet. No comma, only two characters:  100 f
    Enter the width of the room and 'm' for meters, 'f' for feet. No comma, only two characters:  9 m


    274.3199912217603 in square meters, or 2952.7529535119056 in square feet


## Tip Calculator

Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.
___________________________________

P: This is a tip calculator - input for bill amount and tip rate, so two user-submitted variables. Compute the tip, add the tip to the bill, print both. Ignore data validation.

E: The example shows the questions and answers, then the tip and total.

D: No data structure is really relevant here. I'll be using floats down to the hundredths.

A: Input a, input b, a*b = tip, a+tip = total, print 'the tip is \[tip]' and 'the total is \[total]

C:


```python
# Note - I read about the string formatting (:.2f) after a google search. I need to learn/practice it more
bill = float(input('What is the bill? '))
tip_per = float(input('What is the tip percentage? '))

tip = bill * (tip_per / 100)
total = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')
```

    What is the bill?  200
    What is the tip percentage?  20


    The tip is $40.00
    The total is $240.00


## Sum or Product of Consecutive Integers

Write a program that asks the user to enter an integer greater than `0`, then asks whether the user wants to determine the sum or the product of all numbers between `1` and the entered integer, inclusive.

P: The problem asks for a few decision points (write a number, determine sum/product), then will loop through numbers in the range, adding or multiplying them as it goes along. 

E: While it doesn't specify, the sample output shows the result being printed, not returned. It also shows "s" and "p" instead of typing out

D: I feel good about a single integer variable to hold the incrementing final value, a range, and a for loop.

A: Get input. for x in range (1, input), if s, final_value += x, else final_value *= x


```python
user_num = int(input('Please enter an integer greater than 0: '))
sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product: ')
final_num = 1

for x in range(2, (user_num+1)):
    if sum_or_product == "s" or sum_or_product == "sum":
        sum_or_product = "sum"
        final_num += x
    else:
        sum_or_product = "product"
        final_num *= x

print(f'The {sum_or_product} of the integers between 1 and {user_num} is {final_num}.')
```

    Please enter an integer greater than 0:  5
    Enter "s" to compute the sum, or "p" to compute the product:  s


    The sum of the integers between 1 and 5 is 15.


The solution offered set up a few functions. For the sum it directly ran through the range as in `sum(range(1, target_num+1))` which s nicer than mine. It also suggested building in some data validation, so I'll redo with that. 


```python
def get_sum(user_num):
    return sum(range(1, user_num+1))

def get_product(user_num):
    final = 1
    for x in range(1, user_num+1):
        final *= x
    return final

def get_data():
    sum_or_product = input("Would you like to calculate the sum or product? (s/p) ")
    while sum_or_product not in ["s", "p"]:
        print("Invalid input. Please enter 's' for sum or 'p' for product.")
        sum_or_product = input("Would you like to calculate the sum or product? (s/p) ")
    
    user_num = None
    while user_num is None:
        user_num = input("Enter a number: ")
        if not user_num.isdigit() or int(user_num) <= 1:
            print("Invalid input. Please enter an integer greater than zero")
            user_num = None
            continue
        else:
            user_num = int(user_num)
    
    return user_num, sum_or_product

user_num_out, sum_or_product_out = get_data()

if sum_or_product_out == "s":
    print("The sum of the integers between 1 and "
          f"{user_num_out} is {get_sum(user_num_out)}.")
else:
    print("The product of the integers between 1 and "
      f"{user_num_out} is {get_product(user_num_out)}.")
```

    Would you like to calculate the sum or product? (s/p)  s
    Enter a number:  5


    The sum of the integers between 1 and 5 is 15.


## Short Long Short

Write a function that takes two strings as arguments, determins the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

P: Straightforward - input two strings. Count the length of the strings - print the concatenation of short+long+short. For validation purposes, assume the strings are actually going to be different.

E: The examples make clear what to do, and an empty string still counts

D: We just dealing with strings here

A: Input two strings as arguments in a function. Create a reference value of negative infinity. Compare len(str1) with len(str2) and set one as the biggun. return (short + long + short)



```python
def short_long_short(str_1, str_2):
    if len(str_1) > len(str_2):
        long_string = str_1
        short_string = str_2
    else:
        long_string = str_2
        short_string = str_1
    return (short_string + long_string + short_string)

print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))
```

    abcdefghabc
    fghabcdefgh
    xyz


Man, the official solution is smooth, haha:

```
def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1
```

I also really like this person's answer:

```
def short_long_short(str1, str2):
    sorted_strs = sorted([str1, str2], key=len)
    return sorted_strs[0] + sorted_strs[1] + sorted_strs[0]
```

This one is also good:
```
def short_long_short(str1, str2):
    return str2 + str1 + str2 if len(str1) > len(str2) else str1 + str2 + str1
```

## Leap Years (Part 1)

Write a function that takes any year greater than `0` as input and returns True if the year is a leap year or `False` if it's not. For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

* If the year is divisible by 400, it **is** a leap year
* If the year is divisible by 100 but not by 400, it is **not** a leap year
* If the year is divisible by 4 but not by 100, it **is** a leap year
* All other years **are not** leap years.

P: The problem seems pretty straightforward. Take a year as input and return true if it's a leap year, false if it's not. The examples show that it actually means return, not print.

E: The sample code shows the year as an argument passed into the function with a boolean value returned.

D: The return value is boolean.

A: if year % 400 == 0 return true, if year % 100 == 0 and year % 400 != 0 return false. If year % 4 == 0 and year % 100 != 0 return True. else return False



```python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
```

    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True


## Leap Years Part 2

In the previous exercise, we assumed that the Gregorian calendar has been in conintuous use since the year 1. However, the Gregorian calendar wasn't adopted until much later. Prior to that, much of the world used the Julian calendar, which observed leap year every 4 years.

In 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. Update the function from the previous exercise so it uses the Julian calendar prior to 1752 and the Gregorian calendar starting in 1752.


```python
def is_leap_year(year):
    if year < 1752: 
        return year % 4 == 0
    if year >= 1752:    
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
    return year % 4 == 0
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)        
```

    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True


## Multiples of 3 and 5

Write a function that computes the sum of all numbers between `1` and some other number, inclusive, that are multiples of `3` or `5`. For instance, if the supplied number is `20`, the result should be `98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20)`

You may assume that the number passed in is an integer greater than 1

P: SImple enough - sum the numbers in a range that are multiples of 3 or 5. Return the number.

E: The example shows that the final value is returned

D: Take in integers, spit out integer. Use a range in the middle

A: multisum(num) = sum(range(1, num+1, 3)) + sum(range(1, num+1, 5)


```python
def of_3_or_5(number):
    return number % 3 == 0 or number % 5 == 0

def multisum(num):
    count = 0
    for x in range(1, (num+1)):
        if of_3_or_5(x):
            count += x
    return count

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
```

    True
    True
    True
    True


## UTF-16 String Value

Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use `ord` to determine the UTF-16 value of a character.)

P: The problem is straightforward. Write a function that 1. calculates the sum of all the UTF-16 values in the string, then 2. returns that value
E: The examples show that this is a return, not a print. They also show how to work with non ASCII characters by setting a variable
D: I'll be returning an integer
A: Create a sum variable, loop through the string, adding the value of each character to the sum variable, return the sum variable


```python
def utf16_value(strang):
    ret_value = 0
    for char in strang:
        ret_value += ord(char)
    return ret_value

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
```

    True
    True
    True
    True
    True
    True

