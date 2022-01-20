
# coding: utf-8

import mysql.connector
import random
    
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="flask_blog"
)

def select_all():
                            
    cur = mydb.cursor()
    sql ='''SELECT * FROM flask_blog.user_info'''

    cur.execute(sql)
    select_all_result = cur.fetchall()

    for x in select_all_result:
        print(x)

def select_limit(n):
    
    cur = mydb.cursor()
    sql ='SELECT * FROM flask_blog.user_info LIMIT %s' %n
    
    cur.execute(sql)
    select_limit_result = cur.fetchall()

    for x in select_limit_result:
        print(x)

def row_count():
    cur = mydb.cursor()
    sql = 'SELECT * FROM flask_blog.user_info'
    
    cur.execute(sql)
    select_all_result=cur.fetchall()
    print(cur.rowcount)
    
def insert(num):
    cur = mydb.cursor()
    sql ='''SELECT * FROM flask_blog.user_info ORDER BY user_id DESC LIMIT 1'''
    cur.execute(sql)
    last_row = cur.fetchone() 
    
    sql2 = "INSERT INTO flask_blog.user_info(USER_EMAIL,BLOG_ID) VALUES (%s,%s)"
    lists=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i in range(num):
        rand_alphabet=random.choice(lists)
        val = ("abcdef"+rand_alphabet,str(int(last_row[2])+1+i))
        cur.execute(sql2, val)
    mydb.commit()
    print(num,"record inserted") 


