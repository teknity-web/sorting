import random

STACKS = 5
SIZE = 5

stacks = [[] for _ in range(STACKS)]

values = [1]*5 + [2]*5 + [3]*5 + [4]*5
random.shuffle(values)

index = 0
for i in range(STACKS):
    while len(stacks[i]) < SIZE and index < len(values):
        stacks[i].append(values[index])
        index += 1

def display():
    print("\nCurrent Bottles:")
    for i in range(STACKS):
        print(f"Bottle {i+1}: {stacks[i]}")

def move(src, dest):
    if len(stacks[src]) == 0:
        print("Source bottle empty")
        return
    
    if len(stacks[dest]) == SIZE:
        print("Destination bottle full")
        return
    
    val = stacks[src].pop()
    stacks[dest].append(val)

def check_win():
    for stack in stacks:
        if len(stack) == 0:
            continue
        if len(set(stack)) != 1:
            return False
    return True

while True:
    display()
    
    if check_win():
        print("🎉 Congratulations! You solved the puzzle!")
        break

    print("\n1. Move Water")
    print("2. Exit")
    
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        s = int(input("From bottle: ")) - 1
        d = int(input("To bottle: ")) - 1
        move(s, d)
    
    elif ch == 2:
        print("Game Over")
        break
