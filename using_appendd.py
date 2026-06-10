records = []

# FIXED: Now both lines use brackets [] to make it one item
records.append(["Shakeebx", 20])
records.append(["Shashbx", 80])

print("--- RAW DATA ---")
print(records)

print("\n--- 3 WAYS TO PRINT RECORDS ---")

# Way 1: Simple Loop (printing the whole sub-list)
print("1. Simple Loop:")
for item in records:
    print(item)

# Way 2: Unpacking (separating name and score)
print("\n2. Separating Name and Score:")
for name, score in records:
    print(f"Name: {name} | Score: {score}")

# Way 3: Joining (turning them into a string)
print("\n3. Format as a list of strings:")
for item in records:
    print(" - ".join(map(str, item)))
