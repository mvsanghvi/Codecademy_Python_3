python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# 1. We are going to write a while loop to iterate over the provided list python_topics.
# First, we will need a variable to represent the length of the list. 
# This will help us know how many times our while loop needs to iterate.
# Create a variable length and set its value to be the length of the list of python_topics.
length = len(python_topics)

# 2. Next, we will require a variable to compare to our length variable to make sure we are able to implement a condition that eventually allows the loop to stop.
# Create a variable called index and initialize the value to be 0.
index = 0

# 3. Let’s now build our loop. We want our loop to iterate over the list of python_topics and on each iteration print "I am learning about <element from python_topics>". For this loop we will need the following components:
#     A condition for our while loop
#     A statement in the loop body to print from our condition
#     A statement in the loop body to increment our index forward.
# The end result should output: 
# I am learning about variables
# I am learning about control flow
# I am learning about loops
# I am learning about modules
# I am learning about classes
# If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise, you may have an infinite loop! 
# If the stop condition for our loop is never met, we will create an infinite loop which stops our program from running anything else. 
# To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.
while index < length:
  print("I am learning about " +python_topics[index])
  index +=1