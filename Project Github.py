import random 
num = random.randint(1,20)

print("Hello, What your name? ")
player_name=input("Enter your name:")
num_of_guesses = 0
print('Greate, '+ player_name+ ' ! I am guessing a number between 1 and 10: ')

while num_of_guesses < 3:
    guess = int(input())
    num_of_guesses += 1
    if guess <num:
        print('Your guess is too low bro!')
    if guess >num:
        print('Your guess is too high brother!')
    if guess == num:
        break
    if guess == num:
        print('Congrats! You guessed the number in '+ str(num_of_guesses)+ ' tries.')
    else:
        print("Game have end! You did not guess the number.\nThe number was " +str(num))