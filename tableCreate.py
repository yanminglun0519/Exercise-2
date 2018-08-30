import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('./wordCount.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''

sql = '''create table wordCount (
        storyWords text,
        count int)'''

cursor.execute(sql)

print("Table created")

# '''使用游标关闭数据库的链接'''
cursor.close()
