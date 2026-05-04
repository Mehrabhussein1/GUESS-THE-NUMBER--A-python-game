import random
print('''\033[1m\033[33mWelcome to the Random Number Guesser Game!\033[0m
In this game, you will be challenged to guess a random number within a certain range based on the difficulty level you choose.
Each difficulty level offers a different range of numbers and a limited number of attempts to guess the correct number.
The less attempts you use, the more points you will earn!
\033[1m\033[35mgame by: Mehrab Hussein\033[0m''')
while(True):
    difficulty = int(input('''Enter the difficulty you want to play on:
1. Easy (The number is between \033[36m1~10\033[0m) || You get \033[36m3\033[0m attempts.
2. Medium (The number is between \033[36m1~20\033[0m) || You get \033[36m5\033[0m attempts.
3. Hard (The number is between \033[36m1~50\033[0m) || You get \033[36m10\033[0m attempts.
4. Exit         
Your Choice (1/2/3/4): '''))

    if difficulty == 1:
        print('''---- Selected: Easy Mode ----
    The correct number is within the range \033[36m1 to 10\033[0m
    You get to take \033[36m3\033[0m attempts.
    Choose your guesses wisely !!''')
        num= random.randint(1,10)

        for i in range(3):
            ans = int(input(f"Attempt {i+1}: "))
            
            if ans == num:
                print("\033[92m" + "Congratulations! Your Guess it Correct" + "\033[0m")
                if i==0:
                    score=10
                elif i==1:
                    score=7
                elif i==2:
                    score=3
                print("\033[95m" + f"Your Score: {score}" + "\033[0m")
                break

            else:
                print("\033[91m" + f"Oops! Seems like you have wasted attempt no.{i+1} !" + "\033[0m")
                if num > ans :
                    print("\033[94m" + f"Hint: Try a bit higher" + "\033[0m")
                elif num < ans:
                    print("\033[94m" + f"Hint: Maybe try a bit lower?" + "\033[0m")
                score= 0
                if i==2:
                    print("\033[91m" + f"You have wasted all {i+1} attempts dumbo (lmao) !" + "\033[0m")
                    print("\033[93m" + f"The correct number was: {num}" + "\033[0m")
                    print("\033[95m" + f"Your Score: {score}" + "\033[0m")

    elif difficulty == 2:
        print('''---- Selected: Medium Mode ----
    The correct number is within the range \033[36m1 to 20\033[0m
    You get to take \033[36m5\033[0m attempts.
    Choose your guesses wisely !!''')
        num= random.randint(1,20)

        for i in range(5):
            ans = int(input(f"Attempt {i+1}: "))
            
            if ans == num:
                print("\033[92m" + "Congratulations! Your Guess is Correct" + "\033[0m")
                if i==0:
                    score=10
                elif i==1:
                    score=9
                elif i==2:
                    score=7
                elif i==3:
                    score=5
                elif i==4:
                    score=3

                print("\033[95m" + f"Your Score: {score}" + "\033[0m")
                break

            else:
                print("\033[91m" + f"Oops! Seems like you have wasted attempt no.{i+1} !" + "\033[0m")
                if num > ans :
                    print("\033[94m" + f"Hint: Try a bit higher" + "\033[0m")
                elif num < ans:
                    print("\033[94m" + f"Hint: Maybe try a bit lower?" + "\033[0m")
                score= 0
                if i==4:
                    print("\033[91m" + f"You have wasted all {i+1} attempts dumbo (lmao) !" + "\033[0m")
                    print("\033[93m" + f"The correct number was: {num}" + "\033[0m")
                    print("\033[95m" + f"Your Score: {score}" + "\033[0m")

    elif difficulty == 3:
        print('''---- Selected: Hard Mode ----
    The correct number is within the range \033[36m1 to 50\033[0m
    You get to take \033[36m10\033[0m attempts.
    Choose your guesses wisely !!''')
        num= random.randint(1,50)

        for i in range(10):
            ans = int(input(f"Attempt {i+1}: "))
            
            if ans == num:
                print("\033[92m" + "Congratulations! Your Guess is Correct" + "\033[0m")
                if i==0:
                    score=10
                elif i==1:
                    score=9
                elif i==2:
                    score=8
                elif i==3:
                    score=7
                elif i==4:
                    score=6
                elif i==5:
                    score=5
                elif i==6:
                    score=4
                elif i==7:
                    score=3
                elif i==8:
                    score=2
                elif i==9:
                    score=1
                print("\033[95m" + f"Your Score: {score}" + "\033[0m")
                break

            else:
                print("\033[91m" + f"Oops! Seems like you have wasted attempt no.{i+1} !" + "\033[0m")
                if num > ans :
                    print("\033[94m" + f"Hint: Try a bit higher" + "\033[0m")
                elif num < ans:
                    print("\033[94m" + f"Hint: Maybe try a bit lower?" + "\033[0m")
                score= 0
                if i==9:
                    print("\033[91m" + f"You have wasted all {i+1} attempts dumbo (lmao) !" + "\033[0m")
                    print("\033[93m" + f"The correct number was: {num}" + "\033[0m")
                    print("\033[95m" + f"Your Score: {score}" + "\033[0m")

    elif difficulty == 4:
        print("\033[92m" + "Thank you for playing! Goodbye!" + "\033[0m")
        break
    
    elif (difficulty > 4 or difficulty < 1):
        print("\033[91m" + "Invalid Input! Please select a valid difficulty level." + "\033[0m")
