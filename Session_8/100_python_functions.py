# Write a Python program to check a list is empty or not
l = []
if not l:
print("List is empty")

# Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
if x not in dup_items:
uniq_items.append(x)
dup_items.add(x)
print(dup_items)

# Write a Python function that takes two lists and returns True if they have at least one common member
def common_data(list1, list2):
result = False
for x in list1:
for y in list2:
if x == y:
result = True
return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))

# Write a Python program to get the difference between the two lists
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

# Write a Python program to find the second smallest number in a list
def second_smallest(numbers):
a1, a2 = float('inf'), float('inf')
for x in numbers:
if x <= a1:
a1, a2 = x, a1
elif x < a2:
a2 = x
return a2
print(second_smallest([1, 2, -8, -2, 0]))

# Write a Python program to find the second largest number in a list.
def second_largest(numbers):
count = 0
n1 = n2 = float('-inf')
for x in numbers:
count += 1
if x > n2:
if x >= n1:
n1, n2 = x, n1
else:
n2 = x
return n2 if count >= 2 else None

print(second_largest([1, 2, -8, -2, 0]))

# Write a Python program to get the frequency of the elements in a list
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

# Write a Python program to convert a list of multiple integers into a single integer
L = [11, 33, 50]
x = int("".join(map(str, L)))
print("Single Integer: ",x)

# Write a Python program to check if all dictionaries in a list are empty or not.
my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))

# Write a Python program to count the number of characters (character frequency) in a string
def char_frequency(str1):
dict = {}
for n in str1:
keys = dict.keys()
if n in keys:
dict[n] += 1
else:
dict[n] = 1
return dict
print(char_frequency('google.com'))

#Write a python program to replace the first character occurence in the later part of the string
def change_char(str1):
char = str1[0]
length = len(str1)
str1 = str1.replace(char, '$')
str1 = char + str1[1:]

return str1

print(change_char('restart'))


# Write a Python function that takes a list of words and returns the longest one
def find_longest_word(words_list):
word_len = []
for n in words_list:
word_len.append((len(n), n))
word_len.sort()
return word_len[-1][1]

print(find_longest_word(["PHP", "python", "zekelabs"]))

# Write a Python program to count the occurrences of each word in a given sentence
def find_longest_word(words_list):
word_len = []
for n in words_list:
word_len.append((len(n), n))
word_len.sort()
return word_len[-1][1]

print(find_longest_word(["PHP", "python", "zekelabs"]))


# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def to_uppercase(str1):
num_upper = 0
for letter in str1[:4]:
if letter.upper() == letter:
num_upper += 1
if num_upper >= 2:
return str1.upper()
return str1

print(to_uppercase('PyThon'))

# Write a Python program to count and display the vowels of a given text

def vowel(text):
vowels = "aeiuoAEIOU"
print(len([letter for letter in text if letter in vowels]))
print([letter for letter in text if letter in vowels])
vowel('zekelabs')

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
n=int(input("Input a number: "))
d = dict()

for x in range(1,n+1):
d[x]=x*x

print(d)

# Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
current[name] = {}
current = current[name]
print(new_dict)

# Write a Python program to sort a list alphabetically in a dictionary.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)

# Write a Python program to match key values in two dictionaries.
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
print('%s: %s is present in both x and y' % (key, value))

# Write a Python program to count the elements in a list until an element is a tuple
num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
if isinstance(n, tuple):
break
ctr += 1
print(ctr)

# Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = ''.join(tup)
print(str)

# Write a Python program to find the repeated items of a tuple
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
count = tuplex.count(4)
print(count)

# Write a Python program to convert a tuple to a dictionary.
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

# Write a Python program to sort a tuple by its float element.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))

# Write a Python program to add member(s) in a set
color_set = set()
color_set.add("Red")
color_set.update(["Blue", "Green"])
print(color_set)

# Write a Python program to create a symmetric difference
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setc = setx ^ sety
print(setc)

# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
if not x % 2:
count_even+=1
else:
count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
for x in range(6):
if (x == 3 or x==6):
continue
print(x,end=' ')
print("\n")

# Write a Python program to get the Fibonacci series between 0 to 50.
x,y=0,1
while y<50:
print(y)
x,y = y,x+y

# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
for col in range(col_num):
multi_list[row][col]= row*col

print(multi_list)

# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence
items = []
for i in range(100, 401):
s = str(i)
if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
items.append(s)
print( ",".join(items


# Write a Python program to create the multiplication table (from 1 to 10) of a number.
n = int(input("Input a number: "))
for i in range(1,11):
print(n,'x',i,'=',n*i)

# Write a Python function to find the Max of three numbers.
def max_of_two( x, y ):
if x > y:
return x
return y
def max_of_three( x, y, z ):
return max_of_two( x, max_of_two( y, z ) )

print(max_of_three(3, 6, -5))

# Write a Python function to sum all the numbers in a list
def sum(numbers):
total = 0
for x in numbers:
total += x
return total
print(sum((8, 2, 3, 0, 7)))

# Write a Python function to multiply all the numbers in a list
def multiply(numbers):
total = 1
for x in numbers:
total *= x
return total
print(multiply((8, 2, 3, -1, 7)))

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def string_test(s):
d={"UPPER_CASE":0, "LOWER_CASE":0}
for c in s:
if c.isupper():
d["UPPER_CASE"]+=1
elif c.islower():
d["LOWER_CASE"]+=1
else:
pass
print ("Original String : ", s)
print ("No. of Upper case characters : ", d["UPPER_CASE"])
print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')

# Write a Python function that takes a list and returns a new list with unique elements of the first list
def unique_list(l):
x = []
for a in l:
if a not in x:
x.append(a)
return x

print(unique_list([1,2,3,3,3,3,4,5]))

# Write a Python program to print the even numbers from a given list
def is_even_num(l):
enum = []
for n in l:
if n % 2 == 0:
enum.append(n)
return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Write a Python function that checks whether a passed string is palindrome or not

def isPalindrome(string):
left_pos = 0
right_pos = len(string) - 1

while right_pos >= left_pos:
if not string[left_pos] == string[right_pos]:
return False
left_pos += 1
right_pos -= 1
return True
print(isPalindrome('aza'))

# Write a Python program to access a function inside a function
def test(a):
def add(b):
nonlocal a
a += 1
return a+b
return add
func= test(4)
print(func(4))

# Write a Python program to detect the number of local variables declared in a function.
def abc():
x = 1
y = 2
str1= "w3resource"

print(abc.__code__.co_nlocals)


# Write a Python program to check number either positive , negative or zero
num = int (input ("Enter Integer Number: "))
if num == 0:
print ("Zero Entered")
elif num > 0:
print ("Positive Number Entered")
elif num < 0:
print ("Negative Number Entered")

# Write a Python program to Check Divisibility of 2 numbers
nominator = int (input ("Enter Nominator: "))
denominator = int (input ("Enter Denominator: "))
if nominator % denominator == 0:
print("{} is completely Divisible by {}".format(nominator, denominator))
else:
print ("{} is not completely Divisible by {}".format(nominator, denominator))

# Write a python program to check whether Entered caharacter is Vowel or not
letter = input ("Enter a Single Character: ")
if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "o" or letter =="O" or letter == "U" or letter == "u":
print ("{} is Vowel".format(letter))
else:
print ("{} is co nsonent (Not Vowel)".format(letter))

# Write a python program to Sum of n positive Integer
n = int (input ("Enter Value of n: "))
sum = 0
x = 0
while x != n+1: #because we need to include n in sum
sum += x
x+=1
print("Sum of n positive Integer till {} is {}".format(n,sum))

# Write a python program to digit sum of a number
Digits = input("Enter a number: ")
sum = int(Digits[0])
number = Digits[0]
for i in Digits[1::]:
sum+= int(i)
number +=" + {}".format(i)
print("Sum of {} is {}".format(number,sum))


# Write a python program to convert decimal to binary
Decimal = input("Enter Number: ")
num = int(Decimal)
Binary =""
while num>=1:
i = num%2
num = num//2
Binary +=str(i)
print ("Binary Equivalent of {} is {}".format(Decimal,Binary[::-1]))


# Write a python program to Count Numbers, Alphabets, and Special Character
Text = input ("Enter Text: ")
letter, number, spaces , special = 0,0,0,0
for i in Text:
if i.isalpha():
letter+=1
elif i.isspace():
spaces +=1
elif i.isnumeric():
number +=1
else:
special+=1
print(" Alphabets = {} \n Numbers = {} \n Space = {} \n Special Chracter = {}".format(letter,number,spaces,special))

# Write a python class Shape and Sub class Square:
class Shape():
def __init__(self,length = 0):
self.length = length
def Area(self):
print("Area of Shape is 0")
class Square (Shape):
def __init__(self,length = 0):
self.length = length
def Area(self):
self.area = self.length*self.length
print("Area of a Square is: {}".format(self.area))
s1 = Square(2)
s1.Area()

# Write a python function to compute 5/0 using try except
try:
print("Division = {}".format(5/0))
except ZeroDivisionError:
print ("5 cannot be divided by O")

# Write a python program to Accept the String and print the words composed of digits only
Text = input ("Enter Text: ")
Digits = ""
for i in Text:
if i.isnumeric():
Digits +=i+" "
print("Digits used in given strings are: {}".format(Digits))

# Write a python program to program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
num = int (input ("Enter Number: "))
sum = 0
for i in range(num+1):
sum += float(i/(i+1))
print ("Sum: {:.2f}".format(sum))

# Write a python program to program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1
def f(n):
if n == 0 :
return 0
else:
return f(n-1)+100
n = int(input("Enter Number: "))
print("f(n-1)+100 = ", f(n))

# Write a python function Password match the required criteria:
def PasswordMatchCriteria(pas):
upper,lower,special,num = 0,0,0,0
for x in pas:
if (len(pas) >= 6) and (len(pas) <=12):
if x.isupper():
upper+=1
elif x.islower():
lower+=1
elif x.isnumeric():
num +=1
elif x.isspace():
j = 0
else:
special += 1
if (upper > 0) and (lower > 0) and (special > 0) and (num > 0):
return True
else:
False
passwords = input("Enter Passwords which are seperated by \",\": ")
password = passwords.split(",")
for i in password:
if PasswordMatchCriteria(i):
print(i)

# Write a python program to define a function with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
def Generator(n):
for i in range(n+1):
if i%7 == 0:
yield i
n = int(input("Enter Number: "))
for i in Generator(n):
print(i,end = " ")

# Write a python program to make a recursive function to get the sum
def rec(n):
if n == 0:
return n
return rec(n-1) + n
n = int(input())
sum = rec(n)
print(sum)

# Write a python program to count the frequency of letters of the string and print the letters in descending order of frequency.
word = input()
dct = {}
for i in word:
dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x: (-x[1],x[0]))
for i in dct:
print(i[0],i[1]

# Write a python program using lambda funtion to square a number
square2 = lambda num: num * num

# Write a python program to uppercase strings using lambda and map
people = ["Darcy", "Christina", "Diana"]
peeps = list(map(lambda name: name.upper(), people))
print(peeps)

# Write a python program to filter names not starting with "a"
names = ['austin', 'penny', 'anthony', 'rihana', 'billy', 'angel']
a_names = list(filter(lambda name: name[0] == 'a', names))
print(a_names)

# Write a python program to return dict with {student:highest score} USING MAP+LAMBDA
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
final_grades = dict(zip(students,map(lambda pair: max(pair),zip(midterms, finals))))

# Write a python function to sum variable number of arguments
def sum_all(*args):
total = 0
for num in args:
total += num
return total

# Write a python program using kwargs
def fav_colors(**kwargs):
''' kwargs comes as a dictionary '''
print(kwargs)
for person, color in kwargs.items():
print(f"{person}'s favorite color is {color}")

fav_colors(sriju="red", faizu="yellow", kabir="black")

# Write a python program to print even length words in a string
def printWords(s):
s = s.split(' ')

for word in s:
if len(word)%2==0:
print(word)

s = "This is a python language"
printWords(s)

# Write a python program which can compute the factorial of a given number.
ef fact(x):
if x == 0:
return 1
return x * fact(x - 1)

x=int(raw_input())
print (fact(x))

# Write a python program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
alues = []
for i in range(1000, 3001):
s = str(i)
if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
values.append(s)
print (",".join(values))

# Write a python program that accepts a sentence and calculate the number of letters and digits.
s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
if c.isdigit():
d["DIGITS"]+=1
elif c.isalpha():
d["LETTERS"]+=1
else:
pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])

# Write a python program using a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
values = raw_input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))


# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
def putNumbers(n):
i = 0
while i<n:
j=i
i=i+1
if j%7==0:
yield j

for i in reverse(100):
print (i)

# Write a python program using a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
def printDict():
d=dict()
d[1]=1
d[2]=2**2
d[3]=3**2
print (d)
printDict()

# Define a class named American which has a static method called printNationality.
class American(object):
@staticmethod
def printNationality():
print ("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()

# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape(object):
def __init__(self):
pass

def area(self):
return 0

class Square(Shape):
def __init__(self, l):
Shape.__init__(self)
self.length = l

def area(self):
return self.length*self.length

aSquare= Square(3)
print (aSquare.area())

# Write a function to compute 5/0 and use try/except to catch the exceptions.
def throws():
return 5/0

try:
throws()
except ZeroDivisionError:
print ("division by zero!")
except Exception, err:
print ('Caught an exception')
finally:
print ('In finally block for cleanup')

# Write a python program for a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
import math
def bin_search(li, element):
bottom = 0
top = len(li)-1
index = -1
while top>=bottom and index==-1:
mid = int(math.floor((top+bottom)/2.0))
if li[mid]==element:
index = mid
elif li[mid]>element:
top = mid-1
else:
bottom = mid+1

return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)

# Write a python program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)

# Write a python program for selection sort
for i in range(len(A)):
min_idx = i
for j in range(i+1, len(A)):
if A[min_idx] > A[j]:
min_idx = j

A[i], A[min_idx] = A[min_idx], A[i]

# Write a python program for implementation of Bubble Sort
def bubbleSort(arr):
n = len(arr)

for i in range(n-1):
for j in range(0, n-i-1):
if arr[j] > arr[j+1] :
arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

# Write a python program to check if a number is an Armstrong number.
n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
print("The number is an armstrong number. ")
else:
print("The number isn't an arsmtrong number. ")

# Write a python program to check if a number is a Perfect number.
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
if(n % i == 0):
sum1 = sum1 + i
if (sum1 == n):
print("The number is a Perfect number!")
else:
print("The number is not a Perfect number!")

# Write a python program to Check if a Number is a Strong Number
sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
i=1
f=1
r=num%10
while(i<=r):
f=f*i
i=i+1
sum1=sum1+f
num=num//10
if(sum1==temp):
print("The number is a strong number")
else:
print("The number is not a strong number")

# Write a python to find LCM of two numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
min1=a
else:
min1=b
while(1):
if(min1%a==0 and min1%b==0):
print("LCM is:",min1)
break
min1=min1+1

# Write python program to find whether-number-power-two
def is_power_of_two(n):
"""Return True if n is a power of two."""
if n <= 0:
return False
else:
return n & (n - 1) == 0


n = int(input('Enter a number: '))

if is_power_of_two(n):
print('{} is a power of two.'.format(n))
else:
print('{} is not a power of two.'.format(n))

#Write a python program to find length of list using recursion
def length(lst):
if not lst:
return 0
return 1 + length(lst[1::2]) + length(lst[2::2])
a=[1,2,3]
print("Length of the string is: ")
print(a)

# write a python program to shuffle the items in a list and print it
from random import shuffle
mylist = [1, 2, 3, 4, 5]
shuffle(mylist)
print(mylist)


# write a python program that adds the elements of a list to a set and prints the set
my_set = {1, 2, 3}
my_list = [4, 5, 6]
my_set.update(my_list)
print(my_set)


# write a python program that prints the circumference of a circle
import math
radius = 10
print(f'Area: {2 * math.pi * radius}')


# write a python program that prints the area of a rectangle
length = 10
width = 5
print(f'Area: {length * width}')


# write a python program that prints the area of a square
side = 5
print(f'Area: {side * side}')


# write a python program to create a dictionary with numbers 1 to 5 as keys and the numbers in english as values
number_dict = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five'
}


# write a python program to remove words less than a specified length from a sentence
sentence = 'this is my sentence and i will write it my way'
minlength = 3
result = [word for word in sentence.split(' ') if len(word) >= minlength]


# write a python program to keep words less than a specified length in a sentence
sentence = 'this is my sentence and i will write it my way'
maxlength = 3
result = [word for word in sentence.split(' ') if len(word) <= minlength]

#### 93

# write a python function that takes a list as an input and converts all numbers to positive numbers and returns the new list
def make_all_positive(nums):
return [num if num > 0 else -num for num in nums]


# write a python function that takes a list as an input and converts all numbers to negative numbers and returns the new list
def make_all_negative(nums):
return [num if num < 0 else -num for num in nums]


# write a python function to return a set of all punctuation used in a string
def get_punctuations(sentence):
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
used_punctuation = set()
for char in sentence:
if char in punctuations:
used_punctuation.add(char)
return used_punctuation


# write a python program to print the words in a sentence in reverse order
sentence = 'the quick brown fox'
words = sentence.split(' ')
words.reverse()
print(' '.join(words))


# write a python program to replace each word in a sentence with the length of the word and print it
sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split(' ')
lengths = [str(len(word)) for word in words]
print(' '.join(lengths))


# write a python program to convert a set to a list
myset = {1, 2, 4, 7}
mylist = list(myset)


# write a python program to convert a list to a dictionary where the key is the index and the value is the item in the list
my_list = [1, 8, 1, 2, 2, 9]
my_dict = {key: value for key, value in enumerate(my_list)}


# write a python function that returns True if the sum of two provided numbers is even
def is_prod_even(num1, num2):
sum = num1 + num2
return not sum % 2


# write a python program to print the first 5 items in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[:5])


# write a python program to print the last 3 items in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[-3:])