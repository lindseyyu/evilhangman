def init_word(): 
	'''Will read a list of words from a text document, take out ones that contain invalid chars or are shorter than 3 letters'''
	import os.path  
	
	wordList = [] #make a list of all words
	
	goodWordList = [] #make a list for the valid words 

	f = open("words.txt",'r') #read file 
	
	fileLines = f.read().splitlines() #each line 
	

	for word in fileLines: #loop through words in each line 
		if len(word) >= 3:
			wordList.append(word)
	
	#will strip bad characters
	characters = ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|","\",""","'","?","/",">",".","<",",","", ";", ":"]

	for x in characters:
		for word in wordList:
			if x not in word:
				goodWordList.append(word)
	
	
	f.close() #close file 
	
	return wordList #return list of words that are valid 

	
def sort_by_length(wordList, length):

	'''sorts the word list by length, returns all words that have the length the user chooses ''' 
	
	longest = max(wordList, key=len)#find the longest word 
	
	
	lengthLongest = len(longest)  #find length of longest 
	
	availWords = [] 
	rightLength = [] #create a list of words that will be the right length
	wordDict = {} #create a word dictionary 
	
	for i in range(3, lengthLongest):
		wordDict[i] = []
		for word in wordList:
			if len(word) == i:
				wordDict[i] += [word] #separate words by length 
	
	for key in wordDict:
		if key == length:
			availWords.append(wordDict[key]) #only words the right length 
			
	for list in availWords:
		for word in list:
			rightLength.append(word)

	return rightLength #return all words that are the right length 
	
	
def sort_family(words, guess): #to separate the families 
	
	'''Will sort words into families based on where their guess is in the letter, or where it isn't
	and returns the largest family, and the list of words in the family(to give them worse chances of winning)'''
	families = {}  #a list for all families 
	rep = [] #will contain the visual representation of the families, with dashes and letters
	
	finalSorted = {} #for the final sorted families 

	
	l = [] #this list will be used to sort the families

	
	
	for word in words: #for words in the wordList 
		families[word] = "" #create a dictionary key for them 
		for letter in word: #loop through each letter in the word 
			if letter != guess:
				families[word] += "-" #if the letter isn't the guess, then it will be rep by "-"
			if letter == guess: #if letter is the guess, it will be rep by the letter 
				families[word] += guess
	for key in families: #for each key in the families 
		rep.append(families[key]) #append to a list for all the dash representations
	for i in rep: #make a l with each type of key (only one for each) 
		if i not in l: 
			l.append(i)
	

	for item in l: #will make a dict with the representations as the key and a list of words for the value 
		finalSorted[item] = []
		for key in families:
			if families[key] == item:
				finalSorted[item] += [key] 
	
	lenDict = {} #will make a dict out of finalSorted, but instead of a list of words, the value is the number of words in the list 
	
	for key in finalSorted:
		lenDict[key] = len(finalSorted[key]) #number of terms is value now 
	

	largestKey = 0 
	
	
	for key in lenDict: 
		if lenDict[key] > largestKey: 
			largestKey = lenDict[key] #find the largestKey 
	
	for key in finalSorted:
		 if len(finalSorted[key]) == largestKey:
		 	largestKey = key  #find the representation of the largestKey 
		 	
	return largestKey, finalSorted[largestKey] #return only the largestKey (family), and the words that go with it 
	
def letter_input(prompt): 
	'''Makes sure their letter guesses are valid'''
	guess = raw_input(prompt).lower() #makes guesslowercase 
	
	while len(guess) != 1 or ord(guess) > 122 or ord(guess) < 97: #makes sure they do not enter an invalid character
		guess = raw_input("Please enter a valid character!").lower()
		
	return guess	

def get_guess(): #gets guess 
	'''function to get the guess of the letter from the user'''
	guess = letter_input("Guess a letter please: ") #uses letter_input 
	
	while guess in guessList:
		guess = letter_input("You've already guessed that letter, silly! Try again: ")
	
	return guess
	
def int_input(prompt):
	'''makes sure the user input is an integer'''
	answer = raw_input(prompt) #to make sure they enter an int 
	try:
		return int(answer)
	except ValueError: #except the value error if not int, and ask again
		return int_input("Please enter a valid number please: ") 
		
def guess_input(prompt):

	guess = int_input(prompt) #uses int input to make it an int 
			
	if 26 > int(guess) > 0:
		return guess
	if int(guess) >= 26:
		while int(guess) >= 26: #if they try to ask for more guesses than in the alphabet 
			guess = int_input("Are you serious?!! You can't have that many guesses!! Have some faith in yourself! Try again:  ") #allows user to input another number 
	if int(guess) < 0:
		while int(guess) < 0:
			guess = int_input("Are you serious?!! You can't have negative guesses! Try again:  ") 

	return guess

def length_input(prompt, wordList): #to ask for the length the user would like to use 
	'''asks for the length the user would like to use for the word'''
	
	length = int_input(prompt) #uses int input 
	
	wordLengthList = []
	
	
	for word in wordList:
		wordLengthList.append(len(word))
	
	if int(length) in wordLengthList: #if the cell they entered is contained in the open space list, return the space
		return length
	else:
		while int(length) not in wordLengthList: #if space is not open
			length = int_input("My sincere apologies, I don't seem to have any words of that length!! Try again:  ") #allows user to input another number 
	return length	
		

	
def check_game(numGuesses, guessAmount, wordList):#will check the game, make sure the user has not won or lost yet
	
	'''checks to see if the game should end or not- either the user loses or wins'''
	
	if numGuesses == guessAmount: #if they run out of guesses 
		return "lose" 
		
	if "-" not in dash: #if they figured out the whole word 
		return "win"
		
	else:
		return True 

def change_dash(dash, largestKey, guess):
	'''changes what the representation of the word is, based on the user's guess and the largest family'''
		
	dashList = []  
	keyList = []
	
	for char in largestKey: #takes representation of largest key 
		keyList.append(char)
	
	for char in dash: #takes previous dash representation 
		dashList.append(char)
		
	
	if guess in keyList: 
		
		for i in keyList: #loop through each letter 
		
			if i == guess:
				dashList[keyList.index(i)] = guess #changes the dash rep
				keyList[keyList.index(i)] = "" #just in case there is a double letter 
				
		return ''.join(dashList) #joins the list into string 
		

	else:
		return dash  #if it doesn't change, keep the previous dash 
 
	
	
#####Main Program

print ("Welcome to Hangman. Get ready to test your intellectual prowess! \n I am sure you'll do great :) ")


numGuesses = 0 #set number of guesses to 0 

wordList = init_word() #develop list of words from text

length = length_input("How long do you want the word to be?: ", wordList) #asks for the length they would like 

guessAmount = guess_input("How many guesses would you like? ") #asks how many guesses they want 

rightLength = sort_by_length(wordList, length) #sort the list of words with the right length 

print "This is your word:" + ("-") * int(length) #show them the first dash rep.

dash = ("-") *int(length) #set first dash to word before they make any guesses 

guessList = [] #to keep track of previous guesses

guess = get_guess() #get first letter they guess
guessList.append(guess) #add to guess list 

playing = True #set playing to true 

wordList = rightLength  #the new wordList = rightLength (the list of right length words) 


while playing == True: #will go until playing is no longer true 
	sort_family(wordList, guess) #sort family of wordList based on user guess 
	largestKey, wordList = sort_family(wordList, guess)  #get the largestKey (family) and the words that come with it 
	dash =  change_dash(dash, largestKey, guess) #change the dash if necessary
	if guess not in dash: #if the guess isn't in it, 
		numGuesses += 1  #add to number of guesses 
		print ("Sorry, that letter wasn't in the word! But I bet your next guess will be! \n")
	else:
		print ("Nice guess! You must be psychic. \n")  #don't add anything to num of guesses 
	
	print ('\033[1m' + dash) #print out representation of word (in bold!) 
	print ('\033[0m')
	
	
	playing = check_game(numGuesses, guessAmount, wordList) #check to see if they won or lost 
	if playing != "lose" and playing != "win": #if not, then...
	
		print "\033[92m"+"You have " + str(guessAmount - numGuesses) + " guesses left." + "\033[0m" #tell them how many guesses they have
		print "\033[94m"+ "Previous guesses: " + ",".join(guessList)+"\033[0m" #tell them what their previous guesses were 
		guess = get_guess() #get guess again 
		guessList.append(guess) #append guess 
	
 
if playing == "lose": #if they lost
	print ("Sorry, looks like you lost :( . There is always next time. As they say, \"The phoenix must burn to emerge.\" ")
	print ("The correct word was " +  str(wordList[0]) + "-who would've guessed that?")
if playing == "win": #if they won 
	print ("WOW! You got it, the word was " + str(wordList[0]) + ". I always knew you could do it! " )