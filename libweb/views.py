# -*- coding: utf-8 -*-
#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from databaseop import *


#首页
def homepage(req):
    return render(req, 'index.html')
    
#返回图书的信息
def getbook(req):
    bookinfo = GetBookInfo()
    books=[]
    for row in bookinfo:
        node1=row[1]
        node2=GetNameByAuthId(str(row[2]))[1]
        node3=row[5]
        newnode=node1,node2,node3
        books.append(newnode)
    return render_to_response('bookshow.html',{'books':books})

#返回作者信息到页面    
def getauthor(req):
    authorinfo = GetAuthInfo()
    authors=[]
    for row in authorinfo:
        node1=row[1]
        node2=row[2]
        node3=row[3]
        newnode=node1,node2,node3
        authors.append(newnode)
    return render_to_response('authorshow.html',{'authors':authors})

#显示添加作者的页面    
def showauthoradd(req):
    return render(req,'authoradd.html')
   
#保存新增作者信息
def saveauthor(req):
    author = GetAuthCount()[0]+1
    name = req.GET ['authorname']
    age = req.GET['age']
    country = req.GET['country']
    author=int(author)
    age=int(age)
    SaveAuthInfo((author,name,age,country))
    return HttpResponseRedirect('/authorshow')

#显示添加书籍的页面    
def showbookadd(req):
    return render(req,'bookadd.html')

#保存书籍    
def savebook(req):
    isbn = req.GET['isbn']
    title = req.GET ['title']
    author = req.GET['author']
    publisher = req.GET['publisher']
    publishdate = req.GET['publishdate']
    price = float(req.GET['price'])
    authorinfo=GetIdByAuthName('"'+author+'"')
    if authorinfo:
        SaveBookInfo((isbn,title,authorinfo[0],publisher,publishdate,price))
        return HttpResponseRedirect('/bookshow')
    else:
        return HttpResponseRedirect('/lackauthorerror')

def showerrorpage(req):
    return render(req, 'lackauthorerror.html')

#搜索作者        
def searchauthor(req):
    name=req.GET['authorname']
    id=GetIdByAuthName('"'+name+'"')
    if id:
        id=id[0]
	bookinfo = GetBookByAuthId(id)
	books=[]
        for row in bookinfo:
            node1=row[1]
            node2=GetNameByAuthId(str(row[2]))[1]
            node3=row[5]
            newnode=node1,node2,node3
            books.append(newnode)
        return render_to_response('searchauthor.html',{'books':books,'name':name})
    else:
        return render(req, 'lackauthorerror.html')
	
#显示书籍更新信息
def bookupdate(req,n):
    num=n
    bookinfo =GetBookInfo()[int(num)-1]
    isbn=bookinfo[0]
    title=bookinfo[1]
    author= GetNameByAuthId(int(bookinfo[2]))[1]
    publisher=bookinfo[3]
    publishdate=bookinfo[4]
    price=float(bookinfo[5])
    return render_to_response('bookupdate.html',{'isbn':isbn,'title':title,'author':author,'publisher':publisher,'publishdate':publishdate,'price':price,'num':num})

#保存书籍更新后的信息
def updatebook(req):
    num=int(req.GET['num'])
    isbn = req.GET['isbn']
    title = req.GET ['title']
    author = req.GET['author']
    publisher = req.GET['publisher']
    publishdate = req.GET['publishdate']
    price = float(req.GET['price'])
    authorinfo=GetIdByAuthName('"'+author+'"')
    info=GetBookInfo()[num-1]
    DeleteBookInfo(info[0])
    if authorinfo:
        SaveBookInfo((isbn,title,authorinfo[0],publisher,publishdate,price))
        return HttpResponseRedirect('/bookshow')
    else:
        return HttpResponseRedirect('/lackauthor')
        
#删除书籍
def delbook(req,n):
    index = int(n)-1
    info=GetBookInfo()
    num=info[index][0]
    DeleteBookInfo('"'+num+'"')
    return HttpResponseRedirect('/bookshow')
    
#显示书籍具体信息 
def bookdetail(req,n):
    num=n
    bookinfo =GetBookInfo()[int(num)-1]
    isbn=bookinfo[0]
    title=bookinfo[1]
    author= GetNameByAuthId(int(bookinfo[2]))[1]
    publisher=bookinfo[3]
    publishdate=bookinfo[4]
    price=float(bookinfo[5])
    return render_to_response('bookdetail.html',{'isbn':isbn,'title':title,'author':author,'publisher':publisher,'publishdate':publishdate,'price':price,'num':num})
   
#显示作者具体信息
def authordetail(req,n):
    num=n
    authorinfo=GetAuthInfo()[int(num)-1]
    authorname=authorinfo[1]
    age=authorinfo[2]
    country=authorinfo[3]
    bookinfo=GetBookByAuthId(authorinfo[0])
    books=[]
    for row in bookinfo:
        books.append(row[1])
    return render_to_response('authordetail.html',{'authorname':authorname,'age':age,'country':country,'books':books})  