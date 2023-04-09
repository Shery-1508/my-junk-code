
# import imp


# import random


# firstname = "sheharyar"
# lastname = "noor"
# age = 20


# print("my name is ")
# print(firstname)
# print(lastname)
# print(type(lastname))
# print("age ")
# print(age)
# print(type(age))

# sentence = ("my","name","is","sheharyar","noor")
# print(sentence)

# s1,s2,*s3,s4 = sentence

# print(s1 ,  s2  ,s3,  " " +s4 + " ")


# print("random number is ",random.randrange(10,51))

# print(len(sentence[3]))

# text = input("Enter your Name \n ")

# if "sheharyar"  in text:
#     ot = "Valid "
#     print("Hellooo me")
# else:
#     ot = "Invalid Entity Please Leave"
#     print("not me")

# print(text[6:18])

# output = """ You Entered Name {}
#             You are {}
#             Programe 
#             test
#             successfully"""
# print(output.format(text,ot))

# print(text.center(250))

# x = input("enter alphabet/word that you want to count :")
# cnt = text.count(x)

# print(x,"appears ",cnt,"times in sentence")

# random.randint(1,9)
# from turtle import ycor


# _x=20
# _y=20
# _canvas = [['1','2','3'],['4','5','6'],['7','8','9']]
# _canvas = [[' ' for y in range(_y)] for x in range(_x)]
# for y in range(_x):
#     print(' '.join([col[y] for col in _canvas]))

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       
#different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    temporary = int(you.apples)
    you.apples = me.apples  
    me.apples = temporary
    return you.apples,me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    you.ideas = you.ideas + me.ideas
    me.ideas = you.ideas + me.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))





# import random 

# a = []
# for c in range(205):
#     a.append(random.randint(1,100))

# ad = {}

# for c in a:
#     if c in ad:
#         ad[c] += 1
#     else:
#         ad[c] = 1

# x=0
# xc=''
# for c in ad:
#     if ad[c]>x:
#         x = ad[c]
#         xc = c

# a = list(set(a))

# print(xc,x)

# print(ad)

