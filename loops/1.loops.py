# python,loops are execute a block of code repeatedly.python has two main types of loops: for and while.


# for loop

for i in range(10):
    print ("Number is:", i)
    
    
    
    
    
for i in range(1 ,10, 2):
    print ("Number is:", i)
    
    
for i in range (10,1,-2):
    print ("the number is:", i)
    
    
n=10
for i in range(n):
    print("this number is printed by for loop:", i)
    
    
#list = [1,2,3,4,5,6,7,8,9]

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print("Fruit is:", fruit)
    
    
for i in range(100):
    if i == 50:
        print("Loop is stopped at 50")
        continue  # Skip the rest of the loop

    if i % 2 == 0:
        print("Even Number is:", i)
    else:
        print("Odd Number is:", i)

# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)  
    
    
for i in range(3):
    for j in range (2):
                print(f"i={i}, j={j}")

i = 0
while i < 5:
    print(i)
    i += 1  # increment to avoid infinite loop

for i in range(3):
    print(i)
else:
    print("Loop finished without break")
    
    
    
while True:
    print("This runs forever unless you break")
    break






# questions 

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
        
        
        
for i in range(5):
    print(f"Current number is: {i}")
    
for i in range(10,0,-1):
    print(f"Current number is: {i}")
    
    
i=10
while i>0:
    print(f"Current number is: {i}")
    i -= 1 
    
    

i = 0
while i < 3:
    print("Done")
    i += 1
    
    
    
for i in range(5):
    pass 


def my_function():
    for i in range(5):
        pass  # This is a placeholder for future code
    print("Function completed")