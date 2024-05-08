name=input("Enter name: ")
print("Welcome " + name + " time to play wordgame")

secret_word = "aztu"
guess_string = ""
lives = 4

while lives > 0:
    character_left = 0
    for character in secret_word:
        if character in guess_string:
            print(character)
        else:
            print("-")
            character_left +=1
    if character_left == 0:
        print("you won")
        break
    
    guess = input("Guess a letter: ")
    guess_string += guess
    if guess not in secret_word:
        lives -=1
        print("wrong guess!")
        print(f"You have {lives} left")
        if lives ==0:
            print("you died!,gameover")
