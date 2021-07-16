# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:22:07 2021

@author: Usuario
"""
import random #To choose a random word

WORDLIST_FILENAME = "words.txt" #File with a list of words

def loadWords(file):
    """
    Takes: a file as input
    Returns: a list with english words
    """
    inFile = open(file, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    """
    Takes: a list
    Returns: a random element from it
    """
    return random.choice(wordlist)

wordlist = loadWords(WORDLIST_FILENAME) #Creates list of words
secretWord = chooseWord(wordlist) #Choose a random word"

def isWordGuessed(secretWord, lettersGuessed):
    """
    Checks if secret word has been fully revealed
    ----
    Takes: a word and a the list of letters
    Returns: a boolean
    """
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True        
           
def getGuessedWord(secretWord, lettersGuessed):
    """
    Creates display with guessed letters or empty spaces
    ----
    Takes: word, list of letters
    Returns: string
    """
    new = ""
    for letter in secretWord:
        if letter not in lettersGuessed:
            new += "_ "
        else:
            new += letter + " "
    return new

def getAvailableLetters(lettersGuessed):
    """
    Gives the unused letters (as a string)
    ----
    Takes: list of letters
    Returns: string
    """
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in lettersGuessed:
        abc = abc.replace(letter,"")# FILL IN YOUR CODE HERE...
    return abc

def hangman_graphic(guesses):
    """
    Creates graphics for the poor man
    ----
    Takes: number
    Returns: None
    """
    if guesses == -1: # you won graphic
        print("\n")
        print("       0      ")
        print("     ~~|~~    ")
        print("      / \     ")
        print(" ")
    elif guesses == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif guesses == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif guesses == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif guesses == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    else:   # you lost graphic
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")


def hangman():
    """
    Structure of the game
    ---
    Takes: None
    Returns: None
    """
    secretWord = chooseWord(wordlist) #Choose a random word
    print("\nLet's play HANGMAN")   
    
    # Select the number of players:
    canti = int(input("Please, enter the number of players: "))
    if canti == (2):
        print("Hangman game: Human VS Human\n")
        print("Player 1 will choose a word, Player 2 will guess")
        print("Player 2: please look away while your opponent types\n")
        secretWord = input("PLAYER 1) Choose your word: ")
        print(chr(27) + "[2J") 
        print("The secret word has", len(secretWord), "letters\n" )
    elif canti == 1:
        print(chr(27) + "[2J") 

        print("You'll play against me, the computer\n")
        secretWord = chooseWord(wordlist)
        print("I'm thinking in a word of", len(secretWord), "letters\n" )
    else:
        while canti != 1 and canti != 2:
            print("Player 2: please look away while your opponent types")
            canti = int(input("Please, enter the number of players (1 or 2): "))
    
    # Guessing letters
    counter = 6 #Number of "lives"
    print(f"You have {counter} attempts left to guess")
    lettersGuessed = []
    while counter > 0:
        print("Your avaiable letters are:", getAvailableLetters(lettersGuessed))
        print("\n►", getGuessedWord(secretWord, lettersGuessed))
        
        #Making guesses
        intento = input("Choose a letter: ").lower()
        if len(intento) != 1 or intento not in "abcdefghijklmnopqrstuvwxyz":
            print("Choose ONE letter")
        elif intento in lettersGuessed:
            print("That letter has been choosed before")
        else:
            lettersGuessed += intento 
            
            # If letter is correct
            if intento in secretWord: 
                print("\nNice!\n")                
                if isWordGuessed(secretWord, lettersGuessed):
                    counter = -1
                    hangman_graphic(counter)
                    print("You won your freedom! Enjoy the rest of yout life")
                    break
                hangman_graphic(counter)
            
            #If letter not correct
            else:
                counter -= 1
                hangman_graphic(counter)
                print("Bad choice")
                print(f"{counter} attemps left")
    
    #When no remaining lifes
    if counter == 0:            
        print("")
        print("You have been hanged")
        print("The secret word was", secretWord.upper())

        
####################################################################


# Initialize the game        
hangman()

# Ask if player want to play again
continuar = input("Press 'YES' to play again: ").lower()
while continuar == "yes":
    hangman()
    continuar = input("Press 'YES' to play again: ").lower()
    
