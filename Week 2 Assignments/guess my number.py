print("Please think of a number between 0 and 100!")

LNum = 100
MNum = 50
SNum = 0

print("Is your secret number 50?")

YNum = input(
    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

if YNum not in ["h", "l", "c"]:
    print("Sorry, I did not understand your input.")
    YNum = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

i = 0

while i in range(i + 1):
    if YNum == 'h':
        SNum = SNum
        LNum = MNum
        MNum = (LNum + SNum) // 2
        print("Is your secret number " + str(MNum))
        YNum = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        i = i + 1

    elif YNum == 'l':
        SNum = MNum
        MNum = (LNum + SNum) // 2
        print("Is your secret number " + str(MNum))
        YNum = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        i = i + 1

    elif YNum not in ["h", "l", "c"]:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(MNum))
        YNum = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        i = i + 1

    elif YNum == "c":
        print("Game over. Your secret number was: " + str(MNum))
        break
