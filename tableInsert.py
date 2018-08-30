import sqlite3

import time
F = open('story.txt','r' )
allWords = F.read()
listAll = allWords.split(" ")
f = open('Q1.txt','w')
words = {}

for word in listAll:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


for key, values in words.items():
    f.write(key+' '+str(values)+'\n')


conn = sqlite3.connect('wordCount.db')
cursor = conn.cursor()
start = time.time()
print("Connected")
for key, values in words.items():
    sql = '''insert into wordCount
    (storyWords, count)
    values
    (:key, :value)'''

    cursor.execute(sql,{'key': key, 'value': values})
    conn.commit()
end = time.time()
print("All Data Added")
print(end-start)
cursor.close()