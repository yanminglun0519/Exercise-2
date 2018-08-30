import sqlite3
conn = sqlite3.connect('wordCount.db')
cursor = conn.cursor()

print("Connected")

sql = '''select * from wordCount'''

results = cursor.execute(sql)

all_words = results.fetchall()
for word in all_words:
    print(word)