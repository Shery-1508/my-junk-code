import random 
from termcolor import colored



class Q_DATA:
    
    # ---------------------------- main Q list  ---------------
    q = {   
    # {"question" : ["answer","option","option","option"] }
    "Q. what is your name?": ["sheharyar","sheharyar","sami","shehroze"],
    "Q. Who is the founder of Wikipedia?":["jimmy wales","Jimmy Wales","none of these","Bill gates","Jeff Bezos"],
    "Q. Which type of Programming does Python support?":["all of the mentioned","object-oriented programming","structured programming","functional programming","all of the mentioned"],
    "Q. Which of the following is the correct extension of the Python file?":[".py",".pl",".python",".p",".py"],
    "Q. What was Turkey called before 1923?":["The Ottoman Empire","The Turkish Empire","The Ottoman Empire","Republic of Turkey"],
    "Q. How many Muslim countries are currently member of Group of Twenty (G20)?":["Three","Three","One","Two"," None of These"],
    "Q. Jahangir Khan was a famous player of _________?":["Squash","Cricket","Squash","VolleyBall"],
    "Q. Currently, the largest economy in the world is the economy of":["United States","China","United States","Germany","Russia","India"],
    "Q. The Nobel Prize was awarded for the first time in":["1901","1901","1951","1891"],
    "Q. In the oil industry, one barrel of oil is equivalent to how many litres?":["159","159","120","89","60"],
    "Q. In a very low temperature, which of the following water body will freeze at last?":["Sea water","River water","Canal water","Water in a lake","Sea water"],
    "Q. Wind is caused by _______?":["Difference in atmospheric pressure","Rotation of the Earth","Revolution of the Earth","Difference in atmospheric temperature","Difference in atmospheric pressure"],
    "Q. The science of lightning is called":["Fulminology","Electeorology"," Fulminology","Meteorology","Aerology","Lighthology"],
    "Which":["py","pl","python","p","py"],
    
    }
    
    
    
    #---------------list variables ---------------
    questions= []
    answers = []
    options = []
    
    
    
    #----------- saving to lists -----------------
    for a in q.keys():
        # keys(questions) of "q" dict saving in "questions" list
        questions.append(a)
        # list from corresponding (key)question saving  in "options" list this will make 2d list
        options.append(q[a])
    
    #taking range according to main "options" list len (no sub lists)
    for a in range(len(options)):
        #this will take first element of every list (answers) and save it to "answers" list
        answers.append(options[a][0].lower())
        # removing answers from the list see q dict to get the idea
        options[a].pop(0)
    
    
    #---------------  randomize questions ------------------------ 
    # making simple list same size as number of questions
    randomize_questions = [x for x in range(len(questions))]
    #shuffling list items so that it will be used to call questions randomly
    random.shuffle(randomize_questions)






class QUIZ(Q_DATA):
    # -------------------- variables -----------
    __score     = int(0)
    __right_ans = int(0)
    __wrong_ans = int(0)
    
    # ------------------------  show question  ------------------------
    def showquestion(self,n):
        #saving which randomize (question) number is asked will be used in validating
        self.qno = n
        #creating new local options list to validate input by option number
        self.optionsheet = []
        print(Q_DATA.questions[n])
        #shuffling options for that particular question (asked)
        random.shuffle(Q_DATA.options[n])
        #taking len bcz no. of options may vary
        for a in range(len(Q_DATA.options[n])):
            print(a+1,Q_DATA.options[n][a])
            #saving options in local options list this will be used in validating
            self.optionsheet.append(Q_DATA.options[n][a].lower())
        
        self.input_ans()
    
    
    # ------------------------------  input answer  ------------------------------------
    def input_ans(self):
        print("Ans: ")
        ans = input().lower()
        ans = self.validate_ans(ans)
        #now ans is saved as bool 
        self.scorecounter(ans)
        self.print_output(ans)
        
    
    #------------------------------ validate answer -------------------------------------
    def validate_ans(self,ans):
        if len(ans):  
            #checking by string input
            if ans == Q_DATA.answers[self.qno]:
                print("by opt")
                return True
            # checking by opt number input
            # using len(ans) bcz sometimes all opt are in no. it sometimes causes errors
            elif len(ans) == 1 and self.tointeger(ans): #tointeger is explained below
                # index start from 0 for ans-1 
                if (int(ans)-1) < len(self.optionsheet) : # if user input far big value the the index of opt list
                    if self.optionsheet[int(ans)-1] == Q_DATA.answers[self.qno]:
                        print("by opt.no")
                        return True
            # wrong answe
            else:
                return False
        # no input 
        elif not len(ans):
            print("no input")
            return False
        
    # to check if string is convertible 
    # to int used in above func
    def tointeger(self,ans):
        try:
            int(ans)
            return True
        except ValueError:
            return False
    
    
    
    
    # -------------------------- update score ------------------------------------------
    def scorecounter(self,correct_bool):
        if correct_bool:
            self.__score += 1
            self.__right_ans += 1
        elif not correct_bool:
            self.__wrong_ans += 1
    
    
    # --------------------------------------- OUTPUT ------------------------------
    def print_output(self,correct_bool):
        if correct_bool:
            print(colored("\n     congrats that right by option\n\n","green"))
            print("Score:",colored(f"{self.__score}","blue")," --  --  --  -- right:",colored(f"{self.__right_ans}","green") , "- wrong:",colored(f"{self.__wrong_ans}\n\n","red"))
        if not correct_bool:
            print(colored("\n     meh ... that's wrong\n","red"))
            print("Score:",colored(f"{self.__score}","blue")," --  --  --  -- right:",colored(f"{self.__right_ans}","green") , "- wrong:",colored(f"{self.__wrong_ans}\n\n","red"))
    
    
    # --------------------------- START -------------------------------------
    def start(self):
        for n in Q_DATA.randomize_questions[:10]:
            self.showquestion(n)
    

q = QUIZ()
q.start()








# import random
# from termcolor import colored

# def tointeger(ans):
#     try:
#         int(ans)
#         return True
#     except ValueError:
#         return False


# q = { # "question" : ["answer","option","option","option"]
#     "what is your name?": ["sheharyar","sheharyar","sami","shehroze"],
#     "Your Age?":["18","15","17","18"],
#     "Which type of Programming does Python support?":["all of the mentioned","object-oriented programming","structured programming","functional programming","all of the mentioned"],
#     "Which of the following is the correct extension of the Python file?":[".py",".pl",".python",".p",".py"],
#     }

# questions= []
# answers = []
# options = []


# for a in q.keys():
#     # this will take all the keys(questions) of "q" dict and save it in "questions" list
#     questions.append(a)
#     # taking list from corresponding (key)question and saving it in "options" list this will make 2d list
#     options.append(q[a])

# #taking range according to main "options" list len (no sub lists)
# for a in range(len(options)):
#     #this will take first element of every list (answers) and save it to "answers" list
#     answers.append(options[a][0])
#     # removing answers from the list see line 5 to get idea
#     options[a].pop(0)

# # making simple list same size as number of questions
# randomize_questions = [x for x in range(len(questions))]
# #shuffling list items so that it will be used to call questions randomly
# random.shuffle(randomize_questions)


# class quiz:
#     # to count score
#     _score = int(0)
#     _rightans = int(0)
#     _wrongans = int(0)
    
#     def showquestion(self,n):
#         #saving which randomize (question) number is asked will be used in validating 
#         self.qno = n
#         #creating new local options list to validate input by option number
#         self.optionsheet = []
#         print(questions[n])
#         #shuffling options for that particular question (asked)
#         random.shuffle(options[n])
#         #taking len bcz no. of options may vary
#         for a in range(len(options[n])):
#             print(a+1,options[n][a])
#             #saving options in local options list this will be used in validating see line 59
#             self.optionsheet.append(options[n][a])
    
#     def inputanswer(self):
#         correct = False
#         print("\n\n Answer :")
#         ans = input().lower()
#         if len(ans):
#             #checking by string input
#             if ans == answers[self.qno]:
#                 correct = True
#                 print(colored("\n     congrats that right by option\n\n","green"))
#                 self.scorecounter(correct)
#             # checking by number input
#             elif (tointeger(ans)-1) < len(self.optionsheet) : # if user input far big value the the index size
#                 if self.optionsheet[tointeger(ans)-1] == answers[self.qno]:
#                     correct = True
#                     print(colored("\n     congrats dats right by opt.no\n","green"))
#                     self.scorecounter(correct)
#             # wrong answe
#             else:
#                 correct = False
#                 print(colored("\n     meh ... that's wrong\n","red"))
#                 self.scorecounter(correct)
#         # no input 
#         elif not len(ans):
#             print("no input")
#             self.inputanswer()
    
#     def scorecounter(self,correct):
#         if correct:
#             self._score += 1
#             self._rightans += 1
#             print(f"Score:{self._score}  --  --  --  -- right:",colored(f"{self._rightans}","green") , "- wrong:",colored(f"{self._wrongans}\n\n","red"))
#         elif not correct:
#             self._wrongans += 1
#             print(f"Score:{self._score}  --  --  --  -- right:",colored(f"{self._rightans}","green") , "- wrong:",colored(f"{self._wrongans}\n\n","red"))

# startquiz = quiz()
# for x in range(len(randomize_questions)):
#     startquiz.showquestion(randomize_questions[x])
#     startquiz.inputanswer()









