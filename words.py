#This script will read the file text that you have put in your .txt file and output the most counted words.

filename = input('Enter file:') #Have user enter the file they wish to be scanned
handler = open(filename, 'r') #Open and read into the file
counting = dict() #creates a dictionary in python so it will appear as {} if you type print(counting)

for lines in handler: #for each lines that is being read in the handler
  words = line.split() # split each word and store them as a list in words
  for word in words: for each of the word in the list
    counting[word] = counting.get(word,0)+1 #start the first word at 0 then add +1 everytime we come across the word

#set variables to none or 0 #either works
counter = None 
num_word = None

for word, count in list(counting.items()): #for each word and count in the counting list 
  if counter is None or count > counting: #self explanatory 
    num_word = word # store the word in the list to the num_word
    counter = count # store the count of that word in the list to counter
    
print(num_word,counter)

#This will print out the word that appears the most in the text file.


