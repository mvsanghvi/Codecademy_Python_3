# 1. In script.py, antoher teammate Alex wrote "Who wants to be a Millionaire" question and four options. 
# If the answer is an uppercase or lowercase “A”, then the score goes up. Run the program to check it out.
# Who Wants To Be A Millionaire 💰 

score = 0

option1 = 'Fresca'
option2 = 'V8'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  scor += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")

# 2. Oh no, there are two NameError errors! Can you find them both?
# Who Wants To Be A Millionaire 💰 

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = 'Milk'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  score += 100
  print("\nCorrect!")