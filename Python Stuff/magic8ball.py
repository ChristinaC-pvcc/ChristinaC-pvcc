# Name: Christina C
#   Prog Purpose: This Magic 8-Ball code uses Python tuple since the user
#                   does not have the ability to change the 8-Ball answers
#                   However, the program could have used a Python list
#                   instead of a tuple.
#               NOTE: Tuples use parenthese; lists use braces.

import random

answers_8_ball = ( "As I see it, yes", "Ask again later", "Better not to tell you now",
                   "Cannot predict now", "Concentrate and ask again", "Don't count on it",
                   "It is certain", "It is decidedly so", "Most likely",
                   "My reply is no", "My sources say no",  "Outlook good",
                   "Outlook not so good", "Reply hazy try again", "Signs point to yes",
                   "Very doubtful", "Without a doubt", "Yes",
                   "Yes definitely", "You may rely on it", "No", )

def main():

    print("I am the MAGIC 8-BALL and can answer any YES or NO question!")

    another_question = True
    
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC 8-BALL")
        print("... and now...")
        question = input("\nWhat is your YES or NO question?\nYour Question: ")
        print("The MAGIC 8-BALL says: " + answer)

        is_error = True
        
        while is_error == True:
            askAgain = input("\nWould you like to ask me another question (Y or N)?\nInput Here: ")
            if askAgain.upper() == "N":
                is_error = False
                another_question = False
                
            elif askAgain.upper() != "Y" and askAgain.upper() != "N":
                is_error = True
                print("\n*** Error: not a valid input")
                
            else:
                is_error = False
                another_question = True
            

    print("\nCome back again when you have other important questions.")
    print("... Magic 8-Ball OUT.")

main()
