#Coded By Shashwat Raj
#A program to show the function of stack

stack = [] 
# Pushing elements in stack
print("Enter the element in stack")
print("Enter n/N To stop entring number")
while True :
    z=input()
    if z == "no" or z == "No" or z == "NO" or z=='n' or z=='N' :
        break
    stack.append(z)
    
# Printing the initial stack
print('Initial stack') 
print(stack) 

# Poping elements from Stack
print('\nElements poped from stack:') 
while len(stack) > 0:
    print(stack.pop())

#Printing the final Stack
print('\nStack after elements are poped:') 
print(stack)