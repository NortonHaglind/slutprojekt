from msvcrt import getwch
import os
import functions
import json

player_right = 0

question_no = 0

active = True

exit_key = "q"

total_rounds = 20
print("""
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
 ░▒▓█▓▒▒▓█▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
   ░▒▓██▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░      
                                                                                                                                                                                              
                                                                                                                                                                                              
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░                                                                  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░                                                                 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░    ░▒▓██▓▒░░▒▓██▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░                                                                 
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓██▓▒░         ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░                                                                 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██▓▒░    ░▒▓██▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░                                                                 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓██▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░                                                                 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░        ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░                                                                 
                                                 ░▒▓█▓▒░                                                                                                                                      
                                                  ░▒▓██▓▒░                                                                                                                                    
""")
print("tryck på nåt för start")
getwch()
with open("question.json", "r", encoding="utf-8") as file: #läser in json filen som en variabel

    question_info = json.load(file)


while active:

    for question in question_info: # kör varje fråga en åt gången
        
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

                    if int(player_ans) == question["correct_answer"]: #ser om det är korrekt
                         
                         print(question["correct_answer"])

                         player_right = player_right + 1
                    break
                else:
                    continue
            else:
                continue
        
        with open("question.json", "w", encoding="utf-8") as file: #sparar svaren i json filen
            json.dump(question_info, file, indent=4) 
        if not active:
            break

        if question["question_number"] == total_rounds: #ser om man har kört alla frågor
            os.system("cls")
            print(functions.bcolors.YELLOW + "nu är du klar")
            print(f"{functions.bcolors.YELLOW}du fick {functions.bcolors.BLUE}{player_right}{functions.bcolors.YELLOW}/{functions.bcolors.PURPLE}{total_rounds}")
            active = False

            quit
        
            
                            
             
              

          
