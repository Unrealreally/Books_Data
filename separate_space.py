# A list of fruit to practice with
fruits = ["apple", "banana", "cherry", "date"]

print("--- METHOD 1: The Loop (The Manual Way) ---")
# This goes through the list one by one and adds a space at the 'end'
for fruit in fruits:
    print(fruit, end=" ")
print() # This moves the cursor to a new line at the end


print("\n--- METHOD 2: Unpacking (The Shortcut) ---")
# The * symbol tells Python to "unpack" the list and print every item separated by spaces
print(*fruits)


print("\n--- METHOD 3: Joining (The Pro Way) ---")
# This takes a space " " and "joins" every item in the fruits list into one single string
# This is very flexible! You could change " " to ", " to use commas instead.
result = " ".join(fruits)
print(result)