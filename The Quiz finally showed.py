# QUIZ BY PARV GARG

at=[0,"""Question 1	
Brass gets discoloured in air because of the presence of which of the following gases in air?
Your choices are-
1.Oxygen
2.Hydrogen sulphide
3.Carbon dioxide
4.Nitrogen""","""Question 2 
Which of the following is a non metal that remains liquid at room temperature?
Your choices are-
1.Phosphorous
2.Bromine
3.Chlorine
4.Helium""","""Question 3 
Which of the following is used in pencils?
1.Graphite
2.Silicon
3.Charcoal
4.Phosphorous""","""Question 4 
Which of the following metals forms an amalgam with other metals?
1.Tin
2.Mercury
3.Lead
4.Zinc""","""Question 5
Galvanised iron sheets have a coating of
1.lead
2.chromium
3.zinc
4.tin""","""Question 6
Among the various allotropes of carbon
1.coke is the hardest, graphite is the softest
2.diamond is the hardest, coke is the softest
3.diamond is the hardest, graphite is the softest
4.diamond is the hardest, lamp black is the softest""","""Question 7
Heavy water is
1.deuterium oxide
2.PH7
3.rain water
4.tritium oxide""","""Question 8
Soda water contains
1.carbonic acid
2.sulphuric acid
3.carbon dioxide
4.nitrous acid""","""Question 9
The most important ore of aluminium is
1.galena
2.calamine
3.calcite
4.bauxite""","""Question 10
Permanent hardness of water may be removed by the addition of
1.sodium carbonate
2.alum
3.potassium permanganate
4.lime"""]

ap=[0,"Hydrogen Sulphide","Bromine","Graphite","Mercury","Zinc","diamond is the hardest, graphite is the softest",
    
    "Deuterium oxide","Carbonic Acid","Bauxite","Sodium Carbonate"]
    

aq=[0,"""Question 1
Who is the father of Geometry?
Your choices are-
1.Aristotle
2.Euclid
3.Pythagoras
4.Kepler""","""Question 2
Who was known as Iron man of India?
Your choices are-
1.Govind Ballabh Pant
2.Jawaharlal Nehru
3.Subhash Chandra Bose
4.Sardar Vallabhbhai Patel""","""Question 3
Grand Central Terminal, Park Avenue, New York is the world's
1.Largest railway station
2.highest railway station
3.longest railway station
4.None of the above ""","""Question 4
Entomology is the science that studies
1.Behavior of human beings
2.Insects
3.The origin and history of technical and scientific terms
4.The formation of rocks""","""Question 5
Garampani sanctuary is located at
1.Junagarh, Gujarat
2.Diphu, Assam
3.Kohima, Nagaland
4.Gangtok, Sikkim""","""Question 6
Galileo was an Italian astronomer who
1.developed the telescope
2.discovered four satellites of Jupiter
3.discovered that the movement of pendulum produces a regular time measurement
4.All of the above""","""Question 7
Gravity setting chambers are used in industries to remove
1.SOx
2.NOx
3.suspended particulate matter
4.CO""","""Question 8
Film and TV institute of India is located at
1.Pune (Maharashtra)
2.Rajkot (Gujarat)
3.Pimpri (Maharashtra)
4.Perambur (Tamilnadu)""","""Question 9
Guru Gobind Singh was
1.the 10th Guru of the Sikhs
2.founder of Khalsa, the inner council of the Sikhs in 1699
3.author of Dasam Granth
4.All the above""","""Question 10
The ozone layer restricts
1.Visible light
2.Infrared radiation
3.X-rays and gamma rays
4.Ultraviolet radiation"""]







am=[0,"Euclid","Sardar Vallabhbhai Patel","largest railway station",
    "Insects","Diphu, Assam","All of the above","suspended particulate matter","Pune (Maharashtra)",
    "All the above","Ultraviolet radiation"]

def store(u,c,r):
    fil=open("quiz.txt","a")
    a1="Name:"+details[1]+"\n"
    a2="Class:"+details[2]+"\n"
    a3="You have points:"+str(u)+"\n"
    a4="No of right Answers:"+str(c)+"\n"+"No of Wrong Questions:"+ str(r)+"\n"
    a5="Total no of Question:"+str(c+r)+"\n"
    fil.write("\n"+a1+a2+a3+a4+a5)
    fil.close()

def gap(p):
    if p==0:
        print
    elif p==1:
        print
        print
    elif p==2:
        print
        print
        print
    elif p==3:
        print "*-*"*5
    elif p==4:
        print "___"*5
    elif p==5:
        print "\n"*3
def thanks():
    gap(2)
    print """Thanks for your time.
|Made by: Parv Garg|
|Class:12-A        |"""
    gap(3)
    gap(4)
    gap(2)
    a=raw_input("Enter space to start from beginning and any other key to exit...:)")
    if a==" ":
        start()
    else:
        exit()


def last():
    print
    print "SORRY BUT YOU ARE UNBALE TO COPE UP WITH US,"
    print "This will end now, better luck next time :-)"
    thanks()
def error(a):
    try:
        a=int(a)        
    except ValueError:
        last()
    return a
def report(c,r,u):
    gap(5)
    gap(2)
    gap(4)
    print "|     Your Report"
    print
    print "|     You have points",u
    print "|     No of right Answers=",c
    print "|     No of Wrong Questions=",r
    print "|     Total no of Question=",c+r
    gap(4)
    gap(5)
    store(u,c,r)
def checkg(u,c,r,b,a,f,p):
    if b==f:
            u+=a    
            c+=1
            print "Correct answer is:",am[p]
            print "Your answer is correct, You have points,",u
            return (u,c,r)
    else:
            u-=a
            r+=1
            print "Correct answer is:",am[p]
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                report(c,r,u)
                thanks()
            return (u,c,r)
def checks(u,c,r,b,a,f,p):
    if b==f:
            u+=a    
            c+=1
            print "Correct answer is:",ap[p]
            print "Your answer is correct, You have points,",u
            return (u,c,r)
    else:
            u-=a
            r+=1
            print "Correct answer is:",ap[p]
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                report(c,r,u)
                thanks()
            return (u,c,r)
    

           
def start():
    print "$$$$$$$ So here we are again to test your knowledge and skills $$$$$$$"
    print
    print """           <<<< Rules >>>>
|1.	You start from 100 points.|
|2.	You can decide how much you want to bet for each question.|
|3.	You have to enter only specified commands or the application may collapse.|
|4.	You have to select from General and Science Quiz.|
|Best of Luck.... :):)|
"""
    print """Select your Quiz type:-
            (1) General Knowledge Quiz
            (2) Science Quiz
            """
    print
    a=raw_input("Enter from the above choices:")
    if a== "1":
        gap(3)
        print
        gap(4)
        generalknowlegde(u,c,r)
    elif a=="2":
        gap(3)
        print
        gap(4)
        science(u,c,r)
        
    else:
        gap(2)
        last()
def science(u,c,r):
#-1
    print
    print "Here we will test your science knowledge"
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[1]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=2
        p=1
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-2
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[2]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=2
        p=2
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-3
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[3]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=1
        p=3
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-4
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[4]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=2
        p=4
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-5
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[5]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=3
        p=5
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-6
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[6]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=3
        p=6
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-7
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[7]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=1
        p=7
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-8
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[8]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=1
        p=8
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-9
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[9]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=4
        p=9
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
#-10
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print at[10]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=1
        p=10
        u,c,r=checks(u,c,r,b,a,f,p)
    else:
        last()
    report(c,r,u)
    thanks()

    
    
def generalknowlegde(u,c,r):
#-1
    print
    print "Here we will test your general knowledge"
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet:: ")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[1]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=2
        p=1
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-2
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[2]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=4
        p=2
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-3
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[3]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=1
        p=3
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-4
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[4]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=2
        p=4
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-5
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[5]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=2
        p=5
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-6
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[6]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=4
        p=6
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-7
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[7]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=3
        p=7
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-8
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[8]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=1
        p=8
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()

#-9
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[9]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=4
        
        p=9
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()
#-10
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    a=error(a)
    if 0<=a<=u:
        gap(2)
        print aq[10]
        gap(1)
        b=raw_input("Enter your choice:-")
        b=error(b)
        f=4
        p=10
        u,c,r=checkg(u,c,r,b,a,f,p)
    else:
        last()

    report(c,r,u)
    thanks()
    


u=100
c=r=a=0
name=raw_input("Enter your name:")
clas=str(raw_input("Enter your class:"))
details=[0,name,clas]
start()
