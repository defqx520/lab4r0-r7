# -*- coding: utf-8 -*-
#encoding=utf-8

import MySQLdb
import sae.const 
HOST = sae.const.MYSQL_HOST 
PORT = int(sae.const.MYSQL_PORT)
USER =  sae.const.MYSQL_USER 
PASSWORD = sae.const.MYSQL_PASS 
DBNAME = sae.const.MYSQL_DB 
CHARSET = "utf8"
"""
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = '1234'
DBNAME = 'library'
CHARSET = 'utf8'
"""

#初始化
def initial():
    try:
        con = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor = con.cursor()
        #cursor.execute('create database if not exists '+DBNAME)
        con.select_db(DBNAME)
        cursor.execute('create table Author (AuthorID int not null ,\
                                         Name varchar(100),\
                                         Age int,\
                                         country varchar(100),\
                                         primary key (AuthorID))DEFAULT CHARSET=utf8;')
        cursor.execute('create table Book (ISBN varchar(45) not null,\
                                        Title varchar(45),\
                                        AuthorID int,\
                                        Publisher varchar(45),\
                                        PublishDate varchar(45),\
                                        Price decimal(10,2),\
                                        primary key (ISBN),\
                                        foreign key(AuthorID) references Author(AuthorID))DEFAULT CHARSET=utf8;')
        con.commit()
        cursor.close()
        con.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def GetAuthInfo():
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute('select * from Author')
        info=cursor.fetchall()
        result=[]
        for row in info:
            authorID = row[0]
            name = row[1]
            age = row[2]
            country = row[3]
            newnode = authorID,name,age,country
            result.append(newnode)
        cursor.close()
        con.close()
        return result
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def GetBookInfo():
     try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute('select * from Book')
        info=cursor.fetchall()
        result=[]
        for row in info:
            ISBN = row[0]
            Title = row[1]
            AuthorID = row[2]
            Publisher = row[3]
            PublishDate = row[4]
            Price = row[5]
            newnode = ISBN,Title,AuthorID,PublishDate,Publisher,Price
            result.append(newnode)
        cursor.close()
        con.close()
        return result
     except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def SaveAuthInfo(authorinfo):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("insert into Author values(%s,%s,%s,%s)",authorinfo)
        con.commit()
        cursor.close()
        con.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def SaveBookInfo(bookinfo):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("insert into Book values(%s,%s,%s,%s,%s,%s)",bookinfo)
        con.commit()
        cursor.close()
        con.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def GetIdByAuthName(name):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("select AuthorID from Author where name = "+name)
        info=cursor.fetchone()
        cursor.close()
        con.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def GetNameByAuthId(id):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("select * from Author where AuthorID = "+str(id))
        info=cursor.fetchone()
        cursor.close()
        con.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def GetBookByAuthId(id):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("select * from Book where AuthorID ="+str(id))
        info=cursor.fetchall()
        cursor.close()
        con.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
		
def DeleteBookInfo(isbn):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("delete from Book where ISBN = "+ str(isbn))
        con.commit()
        cursor.close()
        con.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def DeleteBookInfo(isbn):
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("delete from Book where isbn = "+ isbn)
        con.commit()
        cursor.close()
        con.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
				
def GetAuthCount():
    try:
        con=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DBNAME,port=PORT,charset=CHARSET)
        cursor=con.cursor()
        cursor.execute("SELECT MAX(AuthorID) AS LargestOrderPrice FROM Author ")
        info=cursor.fetchone()
        cursor.close()
        con.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
