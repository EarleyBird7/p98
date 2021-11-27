import random
number=random.randint(1,9)
chance=0
print("Guess a number between 1 and 9 >:)")
while chance<5:
    guess=int(input("Enter your guess"))
    if guess==number:
        print("congradulations you won :D")
        break
    elif guess<number:
        print("your guess was low, guess a number higher than:",guess)
    else:
        print("your guess was high, guess a number lower than:",guess)
        chance+=1
if not chance<5:
    print("you lose! the number was:", number)