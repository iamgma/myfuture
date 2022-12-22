print("Welcome to the Secret Word Game!")

secret_word = "giraffe"
guess = ""
guess_count = 0 
guess_limit = 3 
out_of_guesses = False
 
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit: 
        guess = input("Enter your guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Shucks, you're out of guesses! GAME OVER")
else:
    print("By golly you guessed it! You win!")