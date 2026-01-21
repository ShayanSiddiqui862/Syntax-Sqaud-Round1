import random as rand
target:int= rand.randint(1,50)
y :int= 1
while (True):
    x = int(input("Enter a number to guess"))
    if x > target:
        print('That`s above the target')
        y= y+1
    elif x < target:
        print('That`s below the target')
        y= y+1    
    elif x == target:
        print("Correct you guessed in",y,'attempsts')
        break
    else:
        print("Unable to guess")
        break
