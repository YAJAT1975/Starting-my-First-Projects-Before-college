import random
print("Number Guessing Game")
print("Values Between  1 to 100 will be chosen you have to guess the correct number ")
print("you have 6 guesses")
Number =random.randrange(1,100,1)
i = 1
flag= True
while i<=6:
    nn=int(input())
    if(nn==Number):
        print("correct guess")
        flag = False
        break
    elif(nn<Number):
     print("Higher")
     i=i+1
    else:
     print("Lower") 
     i=i+1
if(flag== True):
    print("Number was " , Number)

