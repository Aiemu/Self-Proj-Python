#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "jp_words", charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# SQL
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

# 片假名 平假名
sql = """create table words(
         ID int,
         Roman  char(20),
         Katakana  char(20),
         Hiragana  char(20), 
         Chinese char(20),
         English char(20),
         Weight int
)"""

cursor.execute(sql)

# 关闭数据库连接
db.close()