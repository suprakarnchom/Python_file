def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

def contains_word(s, word):
    return word in s

# Test the function
print(contains_word("Hello, world!", "world"))  # Returns True
print(contains_word("Hello, world!", "goodbye"))  # Returns False


def not_string(str):
    if len(str) >= 0 and str[:3] == "not":
        return str
    return "not " + str

not_string("hello")  # Returns "is hello"


def missing_char(str, n):
    return str[0:n] + str[n+1:]

missing_char("kitten", 3)  # Returns "ktten"


def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]

front_back("code")  # Returns "eodc"

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result
string_splosion("cola")  # Returns "ccococolcola"

def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False

name = "John"
greeting = "Hello, {}!".format(name)  # This will create the string "Hello, John!"

# Or using f-strings
greeting = f"Hello, {name}!"  # This will also create the string "Hello, John!"

def make_tags(tag, word):
    result = f"<{tag}>" + word + f"</{tag}>"
    return result

make_tags("i", "Hello")  # Returns "<i>Hello</i>"

def rotate_left3(nums):
    return nums[1] + nums[2] + nums[0]

# Test the function
print(rotate_left3([1, 2, 3]))  # Returns [2, 3, 1]

def max_end3(nums):
    max_val = max(nums[0], nums[-1])
    return [max_val, max_val, max_val]

# Test the function
print(max_end3([1, 2, 3]))  # Returns [3, 3, 3]
print(max_end3([11, 5, 9]))  # Returns [11, 11, 11]
print(max_end3([2, 11, 3]))  # Returns [3, 3, 3]

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40 and cigars <= 60
    if not is_weekend:
        return cigars >= 40 and cigars <= 60
    

def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - big * 5 <= small

# Test the function
print(make_bricks(3, 1, 8))  # Returns True
print(make_bricks(3, 1, 9))  # Returns False
print(make_bricks(3, 2, 10))  # Returns True

def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c

# Test the function
print(lone_sum(1, 2, 3))  # Returns 6
print(lone_sum(3, 2, 3))  # Returns 2
print(lone_sum(3, 3, 3))  # Returns 0

def teen_sum(a, b):
    if a >= 13 and a <= 19 or b >= 13 and b <= 19:
        return 19
    return a + b
def fix_teen(n):
    if n == 15 or n == 16:
        return n
    if n >= 13 and n <= 19:
        return 0
    return n

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

# Test the function
print(no_teen_sum(1, 2, 3))  # Returns 6
print(no_teen_sum(2, 13, 1))  # Returns 3
print(no_teen_sum(2, 1, 14))  # Returns 3

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 >= 5:
        return num + (10 - num % 10)
    else:
        return num - (num % 10)

# Test the function
print(round_sum(16, 17, 18))  # Should output: 60


12 + (10 - 12 % 10)  # Returns 20
12 % 10  # Returns 2
10 - 2  # Returns 8

15 + (10 - 15 % 10)  # Returns 20
15 % 10  # Returns 5
10 - 5  # Returns 5


def close_far(a, b, c):
    if abs(b - a) <2 and abs(c- a) >1 and abs(c - b) >1:
        return False
    if abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False
  
def close_far(a, b, c):
    if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    if abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False
   
def make_chocolate(a, b, c):
    n = b*5
    if c % n >= a and c % 5 <= a:
        return c % 5
    if c % n <= a:
        return a
    if c % n == 0:
        return 0
    
    else:
        return -1

make_chocolate(1,1,4)

make_chocolate(4,1,10)

make_chocolate(3,2,10)

make_chocolate(6,2,7)

make_chocolate(4,1,7)

10 % 10
(4, 1, 9)

9 % 5 == 4 

4 / 5

def make_chocolate(small, big, goal):
    big = min(big, goal // 5)
    goal -= big * 5
    if goal <= small:
        return goal
    return -1


data = {
    'users': [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
    ],
    'products': [
    {'id': 101, 'name': 'Product A', 'price': 20},
    {'id': 102, 'name': 'Product B', 'price': 30},
    {'id': 103, 'name': 'Product C', 'price': 25}
    ]
}
  
def transform_data_fn(data):
    transform_users = []
    for user in data['users']:
        user_id = str(user['id'])+ '01'
        reversed_name = user['name'][::-1]
        transform_users.append({'id': user_id, 'name': user['name'] + ' '+ reversed_name})
  
    transform_products = []
    for product in data['products']:
        product_id = (product['id']) % 100
        product_name = product['name'][-1]
        product_price = product['price'] / 10
        transform_products.append({'id': product_id, 'name': product_name, 'price': product_price})
  
    transform_data = {'users': transform_users, 'products': transform_products}
    return transform_data
    
transform_data = transform_data_fn(data)
print(transform_data)

x= 121
n = len(str(x))
def isPalindrome(x):
    n = len(str(x))
    if x[0:n+1] == x[::-1]:
        return True
    else:
        return False
    
isPalindrome(x)

print(n)
class Solution:
    def scoreOfString(self, s: str) -> int:
        h,e,l,o,a,z = 104, 101, 108, 111, 97, 122
        i = 0
        for s in range(len(s)):
            sum = abs(s[i] - s[i+1])
            i += 1
            return sum
