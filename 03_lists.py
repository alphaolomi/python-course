'''
A List is a collection which is ordered and changeable.
Allows duplicate members.
'''

# Create list
numbers = [1, 2, 3, 4, 5]

a= [2,3, 4] # A mixed list
b= [2,2,7, 3.5, "Hello"]    # An empty list
c= []   # A list containing a list
d= [2,[a,b]]    # Join two lists
e= a + b    # A list of integers

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)



# Simple maniplation

x = a[1] # Get 2nd element (0 is first)
y = b[1:3] # Return a sublist
z = d[1][0][2] # Nested lists
b[0] = 42 # Change an element








