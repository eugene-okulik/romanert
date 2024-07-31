correct_answer = 12

while True:
    try:
        user_input = int(input("Try guessing a number in range from 1 to 15: "))
        if user_input != correct_answer:
            print('Try again!')
        else:
            print('You guessed it right!')
            break
    except ValueError:
        print("You realise that's not a number, right?")
