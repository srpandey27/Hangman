# Hangman game
#

# -----------------------------------
# Starter code
# NOTE:

'''
        ---------------I HAVE CREATED MY OWN FUNCTIONS AND MY OWN VARIABLES ALSO APART FROM THE ONES THAT WERE PRESENT IN THE TEMPALATE. HENCE, THERE ARE SOME NEW FUNCTIONS THAT ARE COMPLETELY WRITTEN BY ME AND IS ONLY PRESENT IN MY PROGRAM-------------#
        '''

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of starter code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count=0
    for x in range(0,len(secretWord),1):
      if secretWord[x] in lettersGuessed:
        count=count+1
    
    if count==len(secretWord):
      return True
    else:
      return False

def getGuessedWord(secretWord, lettersGuessed, mistakes):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far. This function also returns the number of guesses remaining for the user and checks whether the guess user enters is present in the word
    '''

    # FILL IN YOUR CODE HERE...
    found=False
    word=""
    word=secretWord
    
    for x in range (0, len(secretWord),1):
      secretWord=secretWord.replace(secretWord[x],"-")
    
    partialWord=secretWord
    for x in range(0,len(lettersGuessed),1):
      secretWord=partialWord
      oldpartialWord=partialWord
      for y in range(0,len(word),1):
        if lettersGuessed[x]==word[y]:
          partialWord=partialWord[:y]
          partialWord=partialWord + lettersGuessed[x] + secretWord[y+1:]
      newpartialWord=partialWord
      if oldpartialWord==newpartialWord:
        print ()
        print ("****INCORRECT GUESS****")
        mistakes=int(mistakes)+1
        guesses_remaining=8-mistakes
        print (guesses_remaining, "guesses remaining!")
        found=True
        incorrect_list(lettersGuessed[x])
        lettersGuessed.remove(lettersGuessed[x])
      if found==True:
        break

    return (partialWord+str(mistakes))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets="ABCDEFGHIJKLMNOPQRSTUVWYZ"
    for x in alphabets:
      for y in lettersGuessed:
        if y.lower()==x.lower():
          alphabets=alphabets.replace(x,"")
      for y in incorrect:    #this code loops through the list of the incorrect letters. the incorrect letter function is my own function.
        if y.lower()==x.lower():
          alphabets=alphabets.replace(x,"")
    return alphabets  #returns the available alphabets
    
def incorrect_list(x):
    '''THIS IS MY OWN FUNCTION THAT CREATES A LIST OF USED LETTERS'''
    incorrect.append(x)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    At the start of the game,  user is known how many 
    letters the secretWord contains.

    The user is asked to supply one guess (i.e. letter) per round.

    The user receives feedback immediately after each guess 
      about whether their guess appears in the computers word.

    After each round, the partially guessed word so far, as well as letters that the user has not yet guessed are displayed to the user
    '''
    mistakes="0"
    print ("The word contains :",len(secretWord), "letters")
    guess=""
    lettersGuessed=[]
    index=0
    result=False
    while result==False and int(mistakes)<8:
      index=index+1
      availableWords=getAvailableLetters(lettersGuessed)
      print ("Available letters :" , availableWords)
      print()
      print ("USED letters:" ,end=' ')
      print (lettersGuessed + incorrect)
      print()
      print ("######################################################")
      print ()
      print ("Enter guess letter:")
      guess=input()
      unused_letter=True
      while unused_letter==True:  #validation check for the input
        if guess in lettersGuessed or guess in incorrect:
          print ("Sorry the letter already exists. Enter another letter")
          print ()
          guess=input()
        else:
          unused_letter=False
      guess=guess.lower()
      lettersGuessed.append(guess)
      partialWord=getGuessedWord(secretWord, lettersGuessed, mistakes)
      print ()
      print (partialWord[:-1])
      
      mistakes=partialWord[-1]
      result=isWordGuessed(secretWord, lettersGuessed)
    if result==False:  #decides the end outcome of the game
      print ("Sorry you lose! Try again later ")
      print ("The word was",secretWord)
    else:
      print ("Congratulations! You win!") 

wordlist = loadWords()
secretWord=chooseWord(wordlist)
global incorrect  #setting up a global variable called incorrect
incorrect=[]
hangman(secretWord)  #calls the hangman game
