# import time
F = open('story.txt','r' )
allWords = F.read()
listAll = allWords.split(" ")
f = open('Q1.txt','w')
words = {}
# start = time.time()
for word in listAll:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
# end = time.time()

for key, values in words.items():
    f.write(key+' '+str(values)+'\n')
# print(end-start)

check = str(input("Please enter the word you want to check: "))
if check in words:
    print("Occurrence: "+str(words[check]))
else:
    print("Occurrence: 0")