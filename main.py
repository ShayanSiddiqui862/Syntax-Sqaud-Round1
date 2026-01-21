# Task1 (Round1)
import random as rand
target:int= rand.choices(1,50)
print(type(target))
y :int= 5
x:int = input("Enter a number to guess")
for i in range(1,y):
    
    if (x > target):
        print('That`s above the target')
    elif (x < target):
        print('That`s below the target')    
    elif(x == target):
        print("Correct you guessed in",{y},'attempsts')
    else:
        print("Unable to guess")