# =========================================================================
# PYTHON FUNDAMENTALS AND ALGORITHMS (A Comprehensive Beginner File)
# =========================================================================

import cmath # Needed for solving quadratic equations
import sys   # Optional: For basic error handling or system limits

print("=====================================================")
print("             SIMPLE PYTHON PROGRAMS (EXPANDED)       ")
print("=====================================================")


# --- 1. Prime Number Check (Correct Simple Loop) ---
# Checks if a number has any divisors other than 1 and itself.
print("\n--- 1. Prime Number Check ---")
try:
    A = int(input("Enter a number to check if it's prime: "))
except ValueError:
    A = 17 # Default if input fails

is_prime = True

if A <= 1:
    is_prime = False
elif A == 2:
    is_prime = True
else:
    # We only need to check divisibility up to the square root of A for efficiency.
    # We use a simple loop up to A for beginner clarity, skipping the square root optimization.
    for i in range(2, A):
        if A % i == 0:
            is_prime = False
            print(f"  {A} is divisible by {i}. Stopping.")
            break

if is_prime:
    print(f"  RESULT: {A} is a PRIME number.")
else:
    print(f"  RESULT: {A} is NOT a prime number.")
print("-" * 40)


# --- 2. Leap Year Check (Nested If Structure) ---
# A year is a leap year if divisible by 4, unless it's divisible by 100 
# but not by 400.
print("--- 2. Leap Year Check ---")
try:
    year = int(input("Enter a year to check (e.g., 2024, 1900): "))
except ValueError:
    year = 2024 # Default if input fails
    
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"  RESULT: {year} is a LEAP YEAR (divisible by 400).")
        else:
            print(f"  RESULT: {year} is NOT a leap year (divisible by 100 but not 400).")
    else:
        print(f"  RESULT: {year} is a LEAP YEAR (divisible by 4 but not 100).")
else:
    print(f"  RESULT: {year} is NOT a leap year (not divisible by 4).")
print("-" * 40)


# --- 3. Factorial of a Number using Recursion ---
# Factorial(n) = n * (n-1) * ... * 1
print("--- 3. Factorial using Recursion ---")
def factorial(n):
    """Calculates n! using recursion."""
    # Base Case: Stops the recursion
    if n <= 1:
        return 1
    # Recursive Step: Calls itself with a smaller input
    else:
        return n * factorial(n - 1)

try:
    num_fact = int(input("Enter a number for factorial (e.g., 5): "))
except ValueError:
    num_fact = 5
    
if num_fact < 0:
    print("  Factorial is not defined for negative numbers.")
else:
    result = factorial(num_fact)
    print(f"  Calculation: {num_fact}! = {result}")
print("-" * 40)


# --- 4. Simple Name Sorter ---
# Sorts a list of strings alphabetically.
print("--- 4. Simple Name Sorter ---")
names = ["Charlie", "Alice", "Bob", "Eve", "David"]
print(f"  Original list: {names}")

# The .sort() method modifies the list in place (the original list is changed).
names.sort() 

print(f"  Sorted list:   {names}")
print("-" * 40)


# --- 5. Fibonacci Series (Printing first 10 terms) ---
# A series where the next number is the sum of the previous two (0, 1, 1, 2, 3, 5...)
print("--- 5. Fibonacci Series (First 10 terms) ---")
n = 10
a, b = 0, 1
fib_series = []

for i in range(n):
    fib_series.append(a)
    # The key step: simultaneously update a to b, and b to a+b
    a, b = b, a + b 

print(f"  Series: {fib_series}")
print("-" * 40)


# --- 6. Armstrong Number Check (Example: 153) ---
# For a 3-digit number (abc), it's Armstrong if a^3 + b^3 + c^3 = abc.
print("--- 6. Armstrong Number Check (153) ---")
num_arm = 153
sum_cubes = 0
temp = num_arm

# Loop to extract and cube each digit
while temp > 0:
    digit = temp % 10    # Get the last digit
    sum_cubes += digit ** 3 # Cube it and add to sum
    temp //= 10          # Remove the last digit

if num_arm == sum_cubes:
    print(f"  RESULT: {num_arm} IS an Armstrong number (1^3 + 5^3 + 3^3 = {sum_cubes}).")
else:
    print(f"  RESULT: {num_arm} is NOT an Armstrong number.")
print("-" * 40)


# --- 7. Quadratic Equation Solving ---
# Solves for roots of ax^2 + bx + c = 0
print("--- 7. Quadratic Equation Solving (x^2 + 5x + 6 = 0) ---")
a, b, c = 1, 5, 6 
d = (b**2) - (4 * a * c) # Discriminant (d = b^2 - 4ac)

root1 = (-b - cmath.sqrt(d)) / (2 * a) # x1 = (-b - sqrt(d)) / 2a
root2 = (-b + cmath.sqrt(d)) / (2 * a) # x2 = (-b + sqrt(d)) / 2a

print(f"  Equation: {a}x^2 + {b}x + {c} = 0")
print(f"  The roots are: Root 1 = {root1:.2f}, Root 2 = {root2:.2f}")
print("-" * 40)


# --- 8. Sort Array (Bubble Sort) ---
# Simple sorting algorithm: repeatedly steps through the list, compares adjacent 
# elements, and swaps them if they are in the wrong order.
print("--- 8. Bubble Sort ---")
arr = [64, 34, 25, 12, 22, 11]
n = len(arr)
print(f"  Original array: {arr}")

for i in range(n - 1): # Outer loop controls passes
    # Inner loop compares adjacent elements
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Python's elegant swapping syntax
            arr[j], arr[j + 1] = arr[j + 1], arr[j] 

print(f"  Sorted array: {arr}")
print("-" * 40)


# --- 9. Count Occurrences in Array (List) ---
# Uses the simple built-in `.count()` method.
print("--- 9. Count Occurrences in List ---")
data = [1, 2, 2, 3, 4, 2, 5, 2]
target = 2

count = data.count(target)

print(f"  List: {data}")
print(f"  The number {target} occurs {count} times.")
print("-" * 40)


# --- 10. Search Element and Print Position ---
# Uses the built-in `.index()` method.
print("--- 10. Search Element Position ---")
fruits = ["apple", "banana", "cherry", "date"]
item = "cherry"

try:
    # .index() returns the index (position) of the first match
    position = fruits.index(item)
    print(f"  List: {fruits}")
    print(f"  '{item}' found at position (index): {position}")
except ValueError:
    print(f"  '{item}' is not in the list.")
print("-" * 40)


# --- 11. Accept and Check Vowels ---
# Uses the fast Python membership check (`in`).
print("--- 11. Vowel Check ---")
char = 'U' 
print(f"  Checking letter: '{char}'")

# Convert to lowercase and check against the set of vowels
if char.lower() in 'aeiou':
    print(f"  RESULT: '{char}' is a Vowel.")
else:
    print(f"  RESULT: '{char}' is a Consonant.")
print("-" * 40)


# --- 12. Matrix Multiplication (Simple 2x2) ---
print("--- 12. Matrix Multiplication (2x2) ---")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
R = [[0, 0], [0, 0]] 

# Standard matrix multiplication loops: R[i][j] = sum(A[i][k] * B[k][j])
for i in range(2):
    for j in range(2):
        for k in range(2):
            R[i][j] += A[i][k] * B[k][j]

print("  Matrix A * B:")
for row in R:
    print(f"  {row}")
print("-" * 40)


# --- 13. Matrix Transpose ---
# Swapping rows and columns (M x N becomes N x M)
print("--- 13. Matrix Transpose (2x3 to 3x2) ---")
matrix = [[1, 2, 3], 
          [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])

# Initialize the transpose matrix T (cols x rows)
T = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        T[j][i] = matrix[i][j] # The core transpose operation

print("  Original Matrix:")
for row in matrix: print(f"  {row}")
print("  Transposed Matrix:")
for row in T: print(f"  {row}")
print("-" * 40)


# ===============================================
# OBJECT-ORIENTED PROGRAMMING (OOP) CONCEPTS
# ===============================================

print("\n--- 14. Multi-Level Inheritance ---")
class Grandparent:
    def wealth(self):
        print("  Grandparent: Owns a house (Level 1).")

class Parent(Grandparent): # Parent inherits from Grandparent
    def career(self):
        print("  Parent: Has a good career (Level 2).")

class Child(Parent): # Child inherits from Parent
    def hobby(self):
        print("  Child: Loves coding (Level 3).")

c = Child()
c.wealth()  # Accesses Grandparent method
c.career()  # Accesses Parent method
c.hobby()   # Accesses its own method
print("-" * 40)


print("--- 15. Multiple Inheritance ---")
class FlyingCreature:
    def ability1(self):
        print("  I can fly.")

class SwimmingCreature:
    def ability2(self):
        print("  I can swim.")

# Duck inherits from BOTH FlyingCreature and SwimmingCreature
class Duck(FlyingCreature, SwimmingCreature):
    def quack(self):
        print("  Quack!")

d = Duck()
d.ability1()
d.ability2()
d.quack()
print("-" * 40)


print("--- 16. Method Overriding ---")
class Animal:
    def speak(self):
        print("  Animal makes a generic sound.")

class Dog(Animal):
    # This method OVERRIDES the speak() method defined in the parent (Animal)
    def speak(self):
        print("  Woof! (Overridden method)")

a = Animal()
dog = Dog()

a.speak() # Calls Animal's speak()
dog.speak() # Calls Dog's overridden speak()
print("-" * 40)


print("--- 17. Method Overloading (Simulated) ---")
# Python does NOT support true method overloading, but we can simulate it 
# using default parameter values.
class Calculator:
    def add(self, a, b, c=0):
        """Allows calling with 2 or 3 arguments."""
        return a + b + c

calc = Calculator()

# Call 1 (Only 2 arguments used, c defaults to 0)
sum_two = calc.add(5, 3) 
print(f"  Sum of 5 and 3 (2 args): {sum_two}")

# Call 2 (3 arguments used)
sum_three = calc.add(5, 3, 2)
print(f"  Sum of 5, 3, and 2 (3 args): {sum_three}")
print("-" * 40)
