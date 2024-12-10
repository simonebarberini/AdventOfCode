from funzioni import *
safe = 0 
with open("Sfida2/input.txt") as file:
    for line in file:
        value = line.strip().split()
        value = [int(num) for num in value]
        safe += checkSafe(value)

print(safe)
