#!\bin\python3

#Importing modules

import sys #system func and parameters
print(sys.version)
from datetime import datetime as dt #imports as alias and a specific part from module
print(dt.now())


# Advanced strings
my_name = "suvansh"
print (my_name [1])
print (my_name [-1]) #prints the last one

sentence="I Want the world in my hands "

print (sentence [:5]) # prints 5 letters from start
print (sentence [:1])

print (sentence.split()) # splits at every space
print (sentence.split("w")) # splits at w and poor w gets lost

sentence_split = sentence.split()
sentence_join=' '.join (sentence_split)
sentence_join = sentence
print (sentence )
# Escaping Quotation (2 ways)
quote = "he said , she said \" How about me say ?\"" # 1st way to use quotation in print
quote = 'he said , she said " How about me say ?"' # can use single double quotes simul.
print (quote)

too_much_space = "			booh"
print ( too_much_space.strip()) # to strip space

print ("a" in "Apple" ) # to check if a letter is in word (Returns T/F)

letter = 'A'
word = ' Apple'
print (letter.lower() in word.lower()) #Improved

movie = ' Fight club '
print ( ' {} movie made me realize many things '.format(movie) )

# Dictionary - key/ value pairs {}

drinks = { "Whiskey" : 7 , "vodka" : 8 }
print (drinks)
drinks [ "vodka" ]= 9 # price hike mf (uses [] )
print (drinks)
drinks [ ' scotch '] = 4 #add new key-value pair
print (drinks)
drinks.update ({  "desi" : 2  } )# add new key - value pair
print (drinks)
print(drinks.get("desi")) # gets value of key

#adding names as values has to use square brac each time like
# em= {"finance" : ["bob","mob","sob"], }


