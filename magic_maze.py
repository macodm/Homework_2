
num = "SSNN"

n = (input("Guess the 4 directions N,E,S,W:"))


if (n == num):
    print("Great! You guessed the directions in just 1 try! You're a Mastermind!")
else:

    ctr = 0


    while (n != num):

        ctr += 1

        count = 0


        n = str(n)


        num = str(num)


        correct = []


        for i in range(0, 4):

            if (n[i] == num[i]):

                count += 1

                correct.append(n[i])
            else:
                continue

        if (count < 4) and (count != 0):
            print("Not quite. But you did get ", count, " direction(s) correct!")
            print("Also these directions in your input were correct.")

            for k in correct:
                print(k, end=' ')

            print('\n')
            print('\n')
            n = (input("Enter your next choice of directions: "))

            # when none of the digits are guessed correctly.
        elif (count == 0):
            print("None of the directions in your input match.")
            n = (input("Enter your next choice of directions: "))

    if n == num:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
