import random
secret = random.randint(1,10)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have secret!"
print "It is a number from 1 to 9. I'll give you 3 tries."

while guess != secret and tries < 3:
    guess = input("What 's your guess?")
    if guess < secret:
        print " Too low!"
    elif guess > secret:
        print "Too high!"
    tries = tries + 1

if guess == secret:
    print "Avast! You got it! Found my secret, You did!"
else:
    print "No more guesses! Good luck next time.Bye!"
    print "The secret number was",secret
