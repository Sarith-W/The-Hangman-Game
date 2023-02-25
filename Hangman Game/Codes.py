#Importing packages
import random
import mysql.connector
import webbrowser

#Create functions
#Function 1
def game(word_list,lists,level,store,name):
    "This function gets a random word from the list and gives a hint to the player to guess the word based on the difficulty level" 
    random.shuffle(word_list)
    word = random.choice(word_list)

    #Defining global variables
    global wins
    global loses
    global skip
    
    #The hints for the level 'easy'
    if level == "easy":
        if word == "banana":
            hint = "This is a yellow fruit"

        elif word == "hen":
            hint = "They lay eggs"

        elif word == "apple":
            hint = "if you eat this once a day, you can keep your doctor away"

        elif word == "cat":
            hint = "Are you bothered by rats? Then you definietly need this"

        elif word == "telephone":
            hint = "You can't survive a day without using this"

        elif word == "laptop":
            hint = "Type of a computer which you can take anywhere with you"

        elif word == "bottle":
            hint = "This allows you to carry anything liquid"

        elif word == "technology":
            hint = "This is the main reason which connects the world together"

        elif word == "tiktok":
            hint = "This is a social media app where you can upload short videos"

        elif word == "elephant":
            hint = "The largest animal on the land"

        elif word == "school":
            hint = "We get our primary education from here"

        elif word == "butterfly":
            hint = "You can find this living creature commonly in a garden full of flowers"

        elif word == "internet":
            hint = "You need this to connect with the world"

        elif word == "russia":
            hint = "The largest country in the world"

        elif word == "wardrobe":
            hint = "You keep your clothes in here"

        elif word == "mars":
            hint = "The only place in the universe which has water other than the Earth"

        elif word == "antartica":
            hint = "highest, driest, coldest and windiest continent on Earth"

        elif word == "alarm":
            hint = "We use this to wake up early"

        elif word == "aeroplane":
            hint = "By using this, we can travel anywhere on the world"

        elif word == "thieves":
            hint = "We can't sleep peacefully because of them"
            
    #The hints for the level 'hard'
    elif level == "hard":
        if word == "banana":
            hint = "This believed to be as the world's first fruit"

        elif word == "hen":
            hint = "We raise them on farms"

        elif word == "apple":
            hint = "This fruit contains 25% of air"

        elif word == "cat":
            hint = "The only mammal who doesn't taste sweetness"

        elif word == "telephone":
            hint = "This was invented by Alexander Graham Bell"

        elif word == "laptop":
            hint = "These can be used in a smaller space than an ordinary desk computer"

        elif word == "bottle":
            hint = "This comes as plastic, glass, and metal"

        elif word == "technology":
            hint = "People use this to make their daily lives easier"

        elif word == "tiktok":
            hint = "This app is the most downloaded app on the Apple app store in 2019"

        elif word == "elephant":
            hint = "This animal won't forget anything"

        elif word == "school":
            hint = "If a country gets more of these, literacy will increase"

        elif word == "butterfly":
            hint = "This insect use their feet to taste"

        elif word == "internet":
            hint == "More than half of the world's population is using this service"

        elif word == "russia":
            hint = "This country has the biggest nuclear arsenal in the world"

        elif word == "wardrobe":
            hint = "You open this before going to a party"

        elif word == "mars":
            hint = "This is known as the 'Red Planet'"

        elif word == "antartica":
            hint = "This is the largest ice store in the world"

        elif word == "alarm":
            hint = "You need it everyday but you hate it every morning"

        elif word == "aeroplane":
            hint = "An invention of two brothers, which made an evolution in the world"

        elif word == "thieves":
            hint = "Them are the reason why we put cctv cameras"

        
    print("Word   : ",end='')
    for line in range(len(word)):
        print("_",end=' ')

    print("\n",len(word),"turns remain")
    print("**Hint :",hint)
    count = len(word)
    for c in range(20):
        letter = input("\nLetter : ")
        if letter == "exit":
            print("\nThanks for playing with us,",name,"! \nSee you Again!")
            print("\n",special*79)
            
            #Game Stats
            total = wins + loses + skip
            print("\nGame Statistics of",name,"\n")
            print("\tTotal Rounds Played  :",total)
            print("\tTotal Rounds Skipped :",skip)
            print("\tTotal Wins  :",wins)
            print("\tTotal Loses :",loses)
            print("\n**NOTE : The round you exit, will not be count to the total rounds")
            create_db()
            html_file()
            exit()

        elif letter == "skip":
            skip += 1
            print("\nYou skipped the round")
            print("The Word is",word,"\n")
            break

        elif letter.isnumeric() == True:
            print("\nInvalid Input! \nLetter cannot be a number! \nPlease Try Again!")
            create_db()
            exit()
            
        if letter in lists:
            count -= 1
            print("Word   :",end=' ')
            for i in range(len(word)):
                if word[i] in lists:
                    print(word[i],end=' ')
            
                elif word[i] not in lists:
                    print("_",end=' ')
                    
            if letter in word:
                count += 1
                print("\n",count,"turns remain")
                continue
            
            elif letter not in word:
                 print("\n",count,"turns remain")
                 if count == 0:
                    loses += 1
                    print("\noops....You Lost!")
                    print("The Word is",word,"\n")
                    print("Better luck next time!\n")
                    break
                 continue

        
        lists.append(letter)
        count -= 1
        print("Word   :",end=' ')
        for i in range(len(word)):
            if word[i] in lists:
                print(word[i],end=' ')
            
            elif word[i] not in lists:
                print("_",end=' ')


        if letter in word:
            store.append(True)
            count += 1
            print("\n",count,"turns remain")

        elif letter not in word:
            print("\n",count,"turns remain")


        if count == 0:
            loses += 1
            print("\noops....You Lost!")
            print("The Word is",word,"\n")
            print("Better luck next time!\n")
            break

        if store.count(True) == len(set(word)):
            wins += 1
            print("\nCongratulations....You Won!")
            print("The Word is",word,"\n")
            break


#Function 2
def create_db():
    "This function creates a table in the database and inserts data into it"
    "The data will include the record number, Player name, Total rounds played, Total rounds skipped, Total wins and Total loses"
    "These data will be stored per session"
    
    #Defining global variables
    global wins
    global loses
    global skip
    global total
    total = wins + loses + skip


    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
        )

    cursor = db.cursor()

    cursor = db.cursor()

    cursor.execute("SHOW DATABASES")

    #Storing the available databases in a list
    for databases in cursor:
        database_list.append(databases)
    
    #Creating a database, if that database is not in the database_list
    if ("db_test_python",) not in database_list:
        cursor.execute("CREATE DATABASE db_test_python")


    conDict = {'host':'localhost',
               'database':'db_test_python',
               'user':'root',
               'password':''}

    db = mysql.connector.connect(**conDict)

    cursor = db.cursor()

    cursor.execute("SHOW TABLES")

    #Storing the available data tables in a list
    for table_name in cursor:
        table_list.append(table_name)

    #Creating a data table, if that data table is not in the table_list
    if ("game_history",) not in table_list:
        cursor.execute("CREATE TABLE Game_history (Rec_No INT AUTO_INCREMENT PRIMARY KEY, Player_Name VARCHAR(200), Total_Rounds INT(200), Total_Skips INT(200), Total_Wins INT(200), Total_Loses INT(200))")

    #Inserting data into the database
    mySQLText = "INSERT INTO game_history (Rec_No, Player_Name, Total_Rounds, Total_Skips, Total_Wins, Total_Loses) VALUES (%s,%s,%s,%s,%s,%s)"
    myValues = (rec_no, name, total, skip, wins, loses)
    cursor.execute(mySQLText, myValues)

    db.commit()
    print("\n",cursor.rowcount,"Record Added")

    db.close()


#Function 3
def html_file():
    f = open("game_stats.html","w")

    template = f"""<html>
    <head>
    <title>Game Play History</title>
    </head>
    <body>
    <h2>Game Statistics of {name}</h2>

    <p>Total Rounds Played : {total}</p>
    <p>Total Rounds Skipped : {skip}</p>
    <p>Total Wins : {wins}</p>
    <p>Total Loses : {loses}</p>

    </body>
    </html>"""

    f.write(template)
    f.close()

    webbrowser.open("game_stats.html")
   
#----------------Main Program----------------
#Create Variables
word_list = []
letter = 0
lists = []
count = 0
store = []
rounds = 0
choice = 0
hint = 0
level = 0
name = 0
game_name = 0
special = "-"
f = 0
template = 0
wins = 0
loses = 0
skip = 0
total = 0
rec_no = 0
table_list = []
database_list = []

#Storing words
word_list = ["banana","hen","apple","cat","telephone","laptop","bottle","technology","tiktok","elephant","school","butterfly","internet","russia","wardrobe","mars","antartica","alarm","aeroplane","thieves"]

#Menu
game_name = "Welcome to the game HANGMAN!"
print("\n",game_name.center(79,"~"),"\n")
print("We have 20 words for you to guess --- Grab a coffee and be ready to explore your knowledge!\n\n")

#Asking for the player name
name = input("Hello player! What's your name? : ")
print("\n")

#Asking for the difficulty level
print("Game Levels, \n \teasy --> The hints are EASY to guess \n \thard --> The hints are HARD to guess\n")
level = input("Which level do you prefer? (easy/hard)  : ")
print("\n")

#Checking the validity
if level == "easy" or level == "hard":
    pass
else:
    print("Invalid Level! \nLevel must be either 'easy' or 'hard' only \nPlease Try Again!")
    create_db()
    exit()

#Asking for the number of rounds
rounds = input("How many rounds of words do you want to play? : ")

#Checking the validity
if rounds <= "0" or rounds.isnumeric() == False:
    print("\nInvalid Number of Rounds! \nThe number of rounds must only be greater than '0' \nPlease Try Again!")
    create_db()
    exit()
else:
    pass

#Displaying the instructions
print("\n**NOTE : Type only one letter at a time")
print("**NOTE : You can exit from the game anytime you wish by typing the word 'exit'")
print("**NOTE : If you want to skip a round, then simply type the word 'skip'")

#Displaying the record number of the player
rec_no = random.randrange(0,9999)
print("\nPlayer Record Number : ",rec_no)
print("\n",special*79)

#Calling the function for the 1st round
print("\nThis is round 1\n")
game(word_list,lists,level,store,name)

#Calling the function for the remaining rounds    
for a in range(1,int(rounds)):
    choice = input("Do you wish to go to the next round? (yes/no) : ")
    if choice == "yes":
        print("\n",special*79)
        print("\nThis is round",a+1,"\n")
        letter = 0
        lists = []
        count = 0
        store = []
        game(word_list,lists,level,store,name)

    elif choice == "no":
        break

    else:
        print("\nInvalid Input! \nPlease try again by enter either 'yes' or ' no' only!\n")
        create_db()
        exit()

#Good-Bye message
print("\nThanks for playing with us,",name,"! \nSee you Again!\n")
print("\n",special*79)

    
#Displaying Game Stats
total = wins + loses + skip
print("\nGame Statistics of",name,"\n")
print("\tTotal Rounds Played  :",total)
print("\tTotal Rounds Skipped :",skip) 
print("\tTotal Wins  :",wins)
print("\tTotal Loses :",loses)

#Calling the database function
create_db()

#Opening the HTML file which contains the game stats
html_file()


















