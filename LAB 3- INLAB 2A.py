stack = [] 
def top(stack):
  if stack != []:
    print(stack[-1]  + " is top element")
  else:
    print("Stack Empty!!!")
#Function to print size of stack
def size(stack):
  print("Size of stack is " + str(len(stack)))
#Function to check if a stack is empty
def empty(stack):
  if stack == []:
    print("True")
  else:
    print("False")
# append() function is used to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
size(stack)
print(stack)
top(stack)
# pop() function to pop element from stack in LIFO order
print(stack.pop() + " is popped")
print(stack)
empty(stack)
print(stack.pop() + " is popped")
print(stack.pop() + " is popped")
print(stack)
empty(stack)