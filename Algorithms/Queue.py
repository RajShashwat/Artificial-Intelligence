#Coded By Shashwat Raj
#A program to show the function of Queue

queue = [] 
# Pushing elements in Queue
print("Enter the element in queue")
print("Enter n/N To stop entring number")
while True :
    z=input()
    if z == "no" or z == "No" or z == "NO" or z=="n" or z=="N" :
        break
    queue.append(z)
    
# Printing the initial Queue
print('Initial queue') 
print(queue) 

# Poping elements from Queue
print('\nElements dequed from queue:') 
while len(queue) > 0:
    print(queue.pop(0))

#Printing the final Queue
print('\nQueue after elements are dequed:') 
print(queue) 