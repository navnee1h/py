# Simple Fibonacci Series
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

# Armstrong number
num = 153
s = 0
temp = num
while temp > 0:
    digit = temp % 10
    s += digit ** 3
    temp //= 10

if num == s:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#Quadratic equation solving
import cmath
a,b,c=1,5,6
d=(b**2)-(4*a*c)
root1=(-b + cmath.sqrt(d))/(2*a)
root2=(-b - cmath.sqrt(d))/(2*a)
print(f"the roots are {root1} and {root2}")

# Bubble Sort
arr = [64, 34, 25, 12, 22, 11]
n = len(arr)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array (Bubble Sort):", arr)

#Finding all occurences in a list
fruits = ["apple", "banana", "cherry", "date", "apple", "cherry"] # Added duplicates for a better demonstration
item = "cherry"
positions = []

# Iterate through the list using enumerate to get both index (i) and value (fruit)
for i, fruit in enumerate(fruits):
    if fruit == item:
        positions.append(i) # Add the index to the list of positions

if positions:
    print(f"'{item}' found at position(s) (index): {positions}")
else:
    print(f"'{item}' is not in the list.")

# Output for the modified list:
# 'cherry' found at position(s) (index): [2, 5]

# Matrix Multiplication (Simple 2x2)
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
R = [[0, 0], [0, 0]] # Result matrix

for i in range(2):
    for j in range(2):
        for k in range(2):
            R[i][j] += A[i][k] * B[k][j]

print("Matrix A * B:")
for row in R:
    print(row)

# Matrix Transpose
matrix = [[1, 2, 3], 
          [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])

# Initialize transpose matrix with swapped dimensions
T = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        T[j][i] = matrix[i][j] # Swap indices

print("Original Matrix:")
for row in matrix: print(row)
print("Transposed Matrix:")
for row in T: print(row)


