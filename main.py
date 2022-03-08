text = """
a b c a a b
"""

#print(len(text.split()))

#count them using a dictionary. here letters code be keys and count would be value (int)

word_count = {} #make an empty list to hold

#since text.split returns a list, use a For loop to go through that list

#for word in text.split():
#  print(word) #this loops through list and gives you each word

#assign each of the words as a key in the dictionary and provide a value of 1

#for word in text.split():
#  word_count[word] = 1 #pass through the words. make the value equal to 1

#print(word_count) #shows that they are only coming over 1 time? Want to compare it to see if already in dictionary and then add to it. Use an If statement

for word in text.split():
  if word in word_count:
    word_count[word] += 1 # += takes existing number if exists, and adds 1 to it
  else:
    word_count[word] = 1

print(word_count)

#dictionary is case sensitive. but you can use text.lower().split in For loop it will convert them first

getty_addr = """
Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
"""
#count the words in the Gettysburg Address
getty_count = {}

for x in getty_addr.lower().split():
  if x in getty_count:
    getty_count[x] += 1
  else:
    getty_count[x] = 1

print(getty_count)