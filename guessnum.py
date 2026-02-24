import random
print("hello!welcome to the number guessing game.")
print("you have 5 chances to guess the number")

low=int(input("enter the lower bound:"))
high=int(input("enter the upper bound:"))

if low>=high:
    print("invalid range!!upper bound must be greater than lower bound")
    exit()

print(f"\nGuess the number between {low} and {high}")

num=random.randint(low,high)
chances=5
guess_counter=0

while guess_counter<chances:
    try:
        guess=int(input("\nEnter your guess:"))
    except ValueError:
        print("Invalid input.Please enter another number:")
        continue

    guess_counter+=1
    if guess==num:
        print(f"correct guess!number is {num}")
        print(f"You guess it in {guess_counter} attempts")
        break
    elif guess>num:
        print("Too high!!Please try a lesser number")
    else:
        print("Too low!!Please try a greater number")


if guess_counter==chances and guess!=num:
    print(f"Game over!The number to guess was {num}")
