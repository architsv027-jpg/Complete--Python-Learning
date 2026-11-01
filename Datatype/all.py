
# ============================================================
#                 PYTHON DATA TYPES
# ============================================================

# Data Type ka matlab hota hai ki variable ke andar
# kis type ka data store kiya gaya hai.
#
# Python automatically variable ka data type identify karta hai.
#
# type() function ka use karke hum data type check kar sakte hain.
#
# Example:
name = "Archit"
print(type(name))     # Output: <class 'str'>


# ============================================================
# 1. NUMERIC DATA TYPES
# ============================================================

# Numeric data types ka use numbers store karne ke liye hota hai.
# Python mein Numeric ke 3 main types hote hain:
# 1. Integer
# 2. Float
# 3. Complex


# -------------------- A. INTEGER (int) -----------------------

# Integer ka use whole numbers store karne ke liye hota hai.
# Ismein decimal values nahi hoti.
# Positive, Negative aur Zero sab integer ho sakte hain.

age = 20
marks = 85
temperature = -10

print(age)
print(type(age))      # Output: <class 'int'>


# -------------------- B. FLOAT (float) ----------------------

# Float ka use decimal numbers store karne ke liye hota hai.
# Ismein decimal point hota hai.

price = 99.50
percentage = 85.5
temperature = 36.6

print(price)
print(type(price))    # Output: <class 'float'>


# -------------------- C. COMPLEX (complex) -------------------

# Complex number mein Real aur Imaginary parts hote hain.
# Imaginary part ke liye j ka use hota hai.
#
# Example: 3 + 5j
# 3 = Real part
# 5j = Imaginary part

number = 3 + 5j

print(number)
print(type(number))   # Output: <class 'complex'>


# ============================================================
# 2. DICTIONARY (dict)
# ============================================================

# Dictionary data ko Key-Value Pair mein store karti hai.
#
# Key   = Data ka naam
# Value = Actual data
#
# Dictionary mein:
# 1. Data Key-Value format mein hota hai.
# 2. Keys unique hoti hain.
# 3. Values change kar sakte hain.
# 4. New key-value pair add kar sakte hain.
# 5. Dictionary Mutable hoti hai.
#
# GenAI Use:
# API responses, JSON data aur Chat Messages.

student = {
    "name": "Archit",
    "age": 20,
    "course": "GenAI"
}

print(student)

# Dictionary se value access karna
print(student["name"])       # Archit
print(student["course"])     # GenAI

# New value add karna
student["language"] = "Python"

# Existing value update karna
student["age"] = 21

print(student)


# GenAI Example: Chat Message
message = {
    "role": "user",
    "content": "Explain Generative AI"
}

print(message["role"])
print(message["content"])


# ============================================================
# 3. BOOLEAN (bool)
# ============================================================

# Boolean data type mein sirf 2 values hoti hain:
# 1. True
# 2. False
#
# Boolean ka use conditions check karne ke liye hota hai.
#
# GenAI Use:
# API Success/Failure, Login Status, Response Available.

is_student = True
is_logged_in = False

print(is_student)
print(type(is_student))      # Output: <class 'bool'>


# Boolean with If-Else
response_received = True

if response_received:
    print("AI Response Received")
else:
    print("No Response Available")


# ============================================================
# 4. SET (set)
# ============================================================

# Set ka use Unique Values store karne ke liye hota hai.
#
# Set ki Properties:
# 1. Duplicate values allowed nahi hoti.
# 2. Set unordered hota hai.
# 3. Elements add aur remove kar sakte hain.
# 4. Set Mutable hota hai.
# 5. Indexing available nahi hoti.
#
# GenAI Use:
# Duplicate words remove karna aur unique keywords find karna.

numbers = {10, 20, 30, 10, 20}

print(numbers)
print(type(numbers))         # Output: <class 'set'>

# New element add karna
numbers.add(40)

# Element remove karna
numbers.remove(20)

print(numbers)


# Empty Set create karna
# Note: {} empty dictionary banata hai, empty set nahi.
empty_set = set()

print(type(empty_set))


# ============================================================
# 5. SEQUENCE DATA TYPES
# ============================================================

# Sequence ka matlab hota hai multiple values ko
# ek ordered collection mein store karna.
#
# Sequence ke 4 important types:
# 1. String
# 2. List
# 3. Tuple
# 4. Range


# -------------------- A. STRING (str) -----------------------

# String ka use Text ya Characters store karne ke liye hota hai.
#
# String ko single quotes (' ') ya double quotes (" ")
# ke andar likhte hain.
#
# String Immutable hoti hai.
#
# GenAI Use:
# User Prompts, AI Responses, Chat Messages, Documents.

name = "Archit"
language = 'Python'
prompt = "Explain Generative AI"

print(name)
print(type(name))            # Output: <class 'str'>

# String Indexing
# Indexing 0 se start hoti hai.

word = "Python"

print(word[0])               # P
print(word[1])               # y
print(word[-1])              # n

# String Length
print(len(word))             # 6

# String Slicing
print(word[0:3])             # Pyt


# -------------------- B. LIST (list) ------------------------

# List ka use Multiple Values store karne ke liye hota hai.
#
# List ki Properties:
# 1. Multiple values store kar sakte hain.
# 2. Duplicate values allowed hain.
# 3. Different data types store kar sakte hain.
# 4. Ordered collection hoti hai.
# 5. List Mutable hoti hai.
#
# List ko Square Brackets [] mein likhte hain.
#
# GenAI Use:
# Multiple Documents, Text Chunks, Embeddings aur Messages.

subjects = ["Python", "AI", "ML", "GenAI"]

print(subjects)
print(type(subjects))        # Output: <class 'list'>

# List Indexing
print(subjects[0])           # Python
print(subjects[1])           # AI

# List mein new element add karna
subjects.append("Deep Learning")

# List mein element remove karna
subjects.remove("ML")

# List mein element update karna
subjects[0] = "Python Programming"

print(subjects)

# List ki length
print(len(subjects))


# GenAI Example: Multiple Documents
documents = [
    "Python is a programming language",
    "AI can generate text",
    "LLM means Large Language Model"
]

print(documents)


# -------------------- C. TUPLE (tuple) ----------------------

# Tuple bhi List ki tarah Multiple Values store karta hai.
#
# Tuple ki Properties:
# 1. Multiple values store kar sakte hain.
# 2. Duplicate values allowed hain.
# 3. Ordered collection hoti hai.
# 4. Different data types store kar sakte hain.
# 5. Tuple Immutable hota hai.
#
# Tuple ko Parentheses () mein likhte hain.
#
# GenAI Use:
# Fixed Settings aur Fixed Configuration Values.

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))        # Output: <class 'tuple'>

# Tuple Indexing
print(numbers[0])            # 10
print(numbers[1])            # 20

# Tuple ki length
print(len(numbers))

# Tuple ko directly modify nahi kar sakte.
# numbers[0] = 100           # TypeError


# -------------------- D. RANGE (range) ----------------------

# Range ka use Numbers ki Sequence generate karne ke liye hota hai.
#
# Range generally Loops mein use hota hai.
#
# range(5) ka matlab:
# 0, 1, 2, 3, 4
#
# Important:
# Stop value include nahi hoti.
#
# GenAI Use:
# Multiple Documents aur Data Batches par Loop chalana.

numbers = range(5)

print(list(numbers))         # [0, 1, 2, 3, 4]

# Starting aur Ending value
numbers = range(1, 6)

print(list(numbers))         # [1, 2, 3, 4, 5]

# Range with Step
numbers = range(1, 10, 2)

print(list(numbers))         # [1, 3, 5, 7, 9]


# ============================================================
# 6. NONE (NoneType)
# ============================================================

# None ka matlab hota hai ki variable mein abhi koi value nahi hai.
#
# None ek special value hai.
# Iska data type NoneType hota hai.
#
# GenAI Use:
# Jab AI response available na ho ya koi value missing ho.

response = None

print(response)
print(type(response))        # Output: <class 'NoneType'>


# None ke saath If Condition
ai_response = None

if ai_response is None:
    print("No AI Response Available")
else:
    print(ai_response)


# ============================================================
# 7. OTHER BUILT-IN DATA TYPES
# ============================================================

# BYTES (bytes)
# Bytes Immutable Binary Data store karta hai.
# Images, Audio aur Files ke binary data mein useful hai.

data = b"Hello"

print(data)
print(type(data))            # <class 'bytes'>


# BYTEARRAY (bytearray)
# Bytearray Mutable Binary Data store karta hai.

data = bytearray(5)

print(data)
print(type(data))            # <class 'bytearray'>


# FROZENSET (frozenset)
# Frozenset Set ki tarah unique values store karta hai.
# Lekin ye Immutable hota hai.

numbers = frozenset({10, 20, 30})

print(numbers)
print(type(numbers))         # <class 'frozenset'>


# MEMORYVIEW (memoryview)
# Memoryview binary data ko copy kiye bina access karne mein
# help karta hai.

data = memoryview(b"Hello")

print(data)
print(type(data))            # <class 'memoryview'>


# ============================================================
# 8. MUTABLE VS IMMUTABLE
# ============================================================

# MUTABLE:
# Mutable ka matlab hai ki original object ko modify kar sakte hain.
#
# Examples:
# 1. List
# 2. Dictionary
# 3. Set
# 4. Bytearray

# Example: Mutable List

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)               # [100, 20, 30]


# IMMUTABLE:
# Immutable ka matlab hai ki original object modify nahi hota.
#
# Examples:
# 1. Integer
# 2. Float
# 3. Complex
# 4. String
# 5. Tuple
# 6. Boolean
# 7. Bytes
# 8. Range
# 9. NoneType
# 10. Frozenset

# Example: Immutable String

name = "Archit"

# name[0] = "B"              # TypeError

# Hum new string assign kar sakte hain.
name = "Python"

print(name)


# ============================================================
# 9. TYPE CASTING
# ============================================================

# Type Casting ka matlab ek data type ko
# doosre data type mein convert karna hota hai.
#
# Important Type Casting Functions:
#
# int()    = Integer mein convert karta hai.
# float()  = Float mein convert karta hai.
# str()    = String mein convert karta hai.
# bool()   = Boolean mein convert karta hai.
# list()   = List mein convert karta hai.
# tuple()  = Tuple mein convert karta hai.
# set()    = Set mein convert karta hai.

# String to Integer
age = "20"

age = int(age)

print(age)
print(type(age))             # <class 'int'>


# Integer to Float
number = 100

number = float(number)

print(number)                # 100.0


# Integer to String
number = 100

number = str(number)

print(number)
print(type(number))          # <class 'str'>


# List to Tuple
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)                # (10, 20, 30)


# List to Set
numbers = [10, 20, 10, 30]

result = set(numbers)

print(result)                # Unique values


# ============================================================
# 10. TYPE CHECKING
# ============================================================

# type() function se kisi variable ka data type check karte hain.

name = "Archit"
age = 20
price = 99.5
is_student = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))


# isinstance() function se bhi data type check kar sakte hain.

print(isinstance(age, int))       # True
print(isinstance(name, str))      # True
print(isinstance(price, float))   # True


# ============================================================
#                  END OF DATA TYPES
# ============================================================

# REVISION:
#
# Numeric:
# int, float, complex
#
# Dictionary:
# dict
#
# Boolean:
# bool
#
# Set:
# set
#
# Sequence:
# str, list, tuple, range
#
# None:
# NoneType
#
# Other Built-in Types:
# bytes, bytearray, frozenset, memoryview
#
# GenAI ke liye sabse important:
# String, List, Dictionary, Float, Integer, Boolean, None.
#
# Practice these concepts before moving to the next topic.
