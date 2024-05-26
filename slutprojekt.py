from msvcrt import getwch
import os
import functions
import json

player_right = 0

question_no = 0

active = True

exit_key = "q"

total_rounds = 20

with open("question.json", "r", encoding="utf-8") as file:

    question_info = json.load(file)

while active:

    for question in question_info:
        
        os.system("cls")
       
        print(functions.bcolors.YELLOW + functions.bcolors.UNDERLINE +"Fråga" , question["question_number"],":" , question["question"])

        i = 1

        for answer in question["answers"]:

            print(functions.bcolors.DEFAULT + functions.bcolors.BLUE + f"{i}. {answer}")

            i = i + 1

        while True:

            player_ans = getwch()

            if player_ans.lower() == "q":

                active = False

                break
               
            if player_ans.isdigit():

                player_ans == int(player_ans)

                if 0 < int(player_ans) < 5:

                    question["player_answer"] = int(player_ans)

                    if int(player_ans) == question["correct_answer"]:
                         
                         print(question["correct_answer"])

                         player_right = player_right + 1
                    break
                else:
                    continue
            else:
                continue
        
        with open("question.json", "w", encoding="utf-8") as file:
            json.dump(question_info, file, indent=4) 
        if not active:
            break

        if question["question_number"] == total_rounds:
            os.system("cls")
            print(functions.bcolors.YELLOW + "nu är du klar")
            print(f"{functions.bcolors.YELLOW}du fick {functions.bcolors.BLUE}{player_right}{functions.bcolors.YELLOW}/{functions.bcolors.PURPLE}{total_rounds}")
            active = False

            quit
        
            
                            
             
              

          
