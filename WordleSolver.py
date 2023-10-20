"""
    Name: Joshua Ludolf
    Date: 10/18/2022

    Purpose: Wordle Game Solver

    Real life solution:
    Create a list of characters found in the word and in those specific positions.
    Also keeping track of characters not in the word.

    Pseudocode:
    -------------------------------------------------------------------------------------------------------------
    1. Get the number of characters in the word (between 3 and 13)
    2. Ask the user for specific characters in the word (not the specific position)
    3. Ask the user for a specific character in a specific position, restrict the list to only those words.
        a. Loop throught list of words
        b. Compare the words from list to the characters from user input
    4. Ask the user for characters NOT in the words (max of three characters) and 
       then show the list of words that do not have those three characters.
    5. Get user input for if they want to run the program again (creating an while loop and asking user if they want to try again)
    

"""

Infile = open("EnglishOxfordDict.txt","r")

AllWordsList = Infile.read().lower().strip().split("\n")

TryAgain = True

while TryAgain:
    NumberOfLetters = int(input(f"Enter the number of characters in the word (between 3 and 13):"))

    
    FiveLetterList = []
    for Aword in AllWordsList:
        if len(Aword) == NumberOfLetters and Aword.isalpha() and Aword.islower():
            FiveLetterList.append(Aword.strip())
    
    FiveLetterList.sort()

    print(f"Length of PossiblityList: {len(FiveLetterList)}")

    CharactersInWord = str(input(f"Enter characters (lower case) found in the word: ex: rstlne:"))

    while CharactersInWord.islower == False:
        CharactersInWord = str(input(f"Enter characters (lower case) found in the word: ex: rstlne:"))

    FoundList = FiveLetterList[:]


    # To check to see if all letters in user input in the words from the reduce list

    for index in range(len(CharactersInWord)):
        FoundWList = []
        for Aword in FoundList:
            if CharactersInWord[index] in Aword: 
                FoundWList.append(Aword)
            else:
                pass
        FoundList = FoundWList[:]    

    print(f"Number of {NumberOfLetters} letter words with chars {CharactersInWord} are: {len(FoundList)}")

    KnownPos = str(input(f"Enter known position by character, separated by a comma (Ex: 3,a press enter if none):\n"))


    # To get words that have characters in known positions

    PositionList = FoundList[:]

    for index in range(len(KnownPos)):
        
        KnownPosList = []
        
        for Aword in PositionList:
            if KnownPos[index].isdigit() and not KnownPos[index] == (","):

                position = int(KnownPos[index]) - 1 
                letter = str(KnownPos[index + 2])

            if Aword[position] == letter:
            
                KnownPosList.append(Aword)
    
        PositionList = KnownPosList[:]

    index = 0    
    for Aword in PositionList:
        print(f"{Aword}", end= ' ')
        if index == 16:
            print(f"\n")
            index -= 17
        index += 1

            

    print(f"\n")

    # To remove words that have letters not in the word
    # Do the opposite of when we wanted to check to see if the characters are in a word

    NotLetters = input("Enter characters not in word ex:rstln :")

    FinalList = PositionList[:]
    

    for index in range(0,len(NotLetters)):
        
        ResultList = []

        for Aword in FinalList:
           
            if not(NotLetters[index] in Aword):
                ResultList.append(Aword)
                
            
        FinalList = ResultList[:]
    
   
    print(f"\n")
    
    index = 0
    for Aword in FinalList:
        
        print(f"{Aword}", end= ' ')
        if index == 16:
            print(f"\n")
            index -= 17
        index += 1
        
    
    print(f"")

    # To see if the user wants to run the program again or not
    UserResponse = input(f"\nTry again?(y/n):")
    if UserResponse == "y":
        TryAgain = True
    elif UserResponse == "n":
        TryAgain = False
    else:
        while(not(UserResponse == "y" or UserResponse == "n")):
            UserResponse = input(f"\nPlease enter y or n\nTry again?(y/n):")
            if UserResponse == "y":
                TryAgain = True
            elif UserResponse == "n":
                TryAgain = False
    
   