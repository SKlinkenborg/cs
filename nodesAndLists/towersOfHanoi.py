from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = []
stacks.append(left_stack)
stacks.append(right_stack)
stacks.append(middle_stack)

#Set up the Game
num_disks = 0
while num_disks < 3:
  num_disks = int(input("\nHow many disks do you want to play with?\n"))

# Iterate backwards through range of num_disk; range(start, stop, step)
for num in range(num_disks, 0 ,-1):
  # and add them to the left_stack
  left_stack.push(num)

# For towers of hanoi, the number of optimal moves is always (2^Number of Disks) - 1.
num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

#Get User Input
# List each stack in stacks as a possible input option
def get_input():
  # for each item in stacks, get the first letter of the name
  choices = [stack.get_name()[0] for stack in stacks]
  # until a correct option is chosen, ask the player to pick a stack by choice (first letter)
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name() 
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input in choices[i]:
          return stacks[i]
    
#Play the Game