import sqlite3
from termcolor import colored
import time

data = [
{"ans": "A: 1st Moharamm ul haram 1444H", "opt": ["A: 1st Moharamm ul haram 1444H", "B: 2nd Moharamm ul haram 1444H", "C: 8th zill hajj 1443H", "D: 9th zill hajj 1443H"], "ques": "Q: For first time in history, Saudi Arabia replaces Ka'aba's  kiswa(changing of Gilaaf) occurred on which date ?"},
{"ans": "D: Droupadi Murmu", "opt": ["A: Parnab mukherji", "B: Ram nath kovind", "C: Narendra Modi", "D: Droupadi Murmu"], "ques": "Q: Who is current Indian president ?"},
{"ans": "C: United Kingdom", "opt": ["A: China", "B: United States", "C: United Kingdom", "D: Russia"], "ques": "Q: Which country has pledged to ban sale of new petrol and diesel cars by 2030  ?"},
{"ans": "D: Elon Musk", "opt": ["A: Warren Buffet", "B: Jack Maa", "C: Jeff Bezos", "D: Elon Musk"], "ques": "Q: Who is the Fortune\u2019s Businessperson of the Year 2020  ?"},
{"ans": "B: Favorable balance of payment", "opt": ["A: To increase government revenue", "B: Favorable balance of payment", "C: All the above", "D: To stabilize exchange rate"], "ques": "Q: What is the objective of foreign exchange control ?"},
{"ans": "C: Suez Canal ", "opt": ["A: Strait of Malacca", "B: Indus River", "C: Suez Canal ", "D: Red Sea"], "ques": "Q: A ship recently blocked which trade route causing the world economy to lose million of Dollars ?"},
{"ans": "B: Dr. Henry Kissinger", "opt": ["A: Richard Nixon", "B: Dr. Henry Kissinger", "C: Hillary Clinton", "D: None of these"], "ques": "Q: Who acknowledged Pakistan\u2019s pivotal role in establishing Sino-USA relations in 1971 ?"},
{"ans": "A: Cristiano Ronaldo", "opt": ["A: Cristiano Ronaldo", "B: Lionel Messi", "C: Romario", "D: Joseph Bickan"], "ques": "Q: Who has become the highest player to score 770 goals in Football History ?"},
{"ans": "A: Rights of Rivers", "opt": ["A: Rights of Rivers", "B: Rivers for Life", "C: Positive Rivers", "D: Water & Climate"], "ques": "Q: What is the theme of the International Day of Action for Rivers 2021 ?"},
{"ans": "D: Tabuk", "opt": ["A: Uhud", "B: Taif", "C: Badr", "D: Tabuk"], "ques": "Q: The Line is a proposed smart city in Saudi Arabia is located in the area of________ ?"}
]



conn = sqlite3.connect("dataofjsonfile.db")
# crsr.execute('''DROP TABLE IF EXISTS daata''')
conn.execute('''create table if not exists ques(
                ID        INT PRIMARY KEY  NOT NULL,
                questions text,
                Answers   text,
                Options    text
                )''')
conn.commit()

def enterdata():
    for a in range(0,10):
        allopt = data[a]['opt'][0] +' , '+ data[a]['opt'][1] +' , '+ data[a]['opt'][2] +' , '+ data[a]['opt'][3]
        conn.execute("""insert into ques values(?,?,?,?)""",
                    (
                        (a+1),
                        data[a]['ques'],
                        data[a]['ans'],
                        allopt,
                    ))
    conn.commit()

def printdata():
    datatoprint = conn.execute('''SELECT ID,questions,Options,Answers from ques''')
    conn.commit()
    for row in datatoprint:
        print("ID",row[0])
        print (("Question:", row[1][2:]))
        print ("Options = ", row[2])
        print ("Ans = ", row[3], "\n")

contin = 'y'
while(contin != 'n'):
    print("1 : Enter Data to Table")
    print("2 : Print Table")
    x = int(input("enter choice"))
    print(x)
    if(x == 1):
        try:
            enterdata()
        except sqlite3.IntegrityError:
            print(colored("\nData already there...",'red'))
    elif(x == 2):
        printdata()
        print(x)
    else:
        print("wrong entry\n")
    print("\n\nWanna do again y/n")
    contin = input()
print(colored("Bye..  :)",'blue'))
time.sleep(2)
