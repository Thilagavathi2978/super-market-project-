import re
import datetime
import smtplib
import store

f=open("product.txt","r")
txt=f.read()
f=open("bill.txt","a")
f.write("\n****supermarket bill****") 
def fun():
    word=input("enter a Grocergy :")
    if word=="rice":
        x=re.search(word,txt)
        print(x)
        if x:
            store. item1()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word== "oil":
        x=re.search(word,txt)
        print(x)
        if x:
            store.item2()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="sugar":
        z=re.search(word,txt)
        print(z)
        if z:
            store.item3()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="flour":
        a=re.search(word,txt)
        print(a)
        if a:
            store.item4()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                 fun()
    elif word=="dal":
        b=re.search(word,txt)
        print(b)
        if b:
            store.item5()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="soap":
        q=re.search(word,txt)
        print(q)
        if q:
            store.item6()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="butter":
        c=re.search(word,txt)
        print(c)
        if c:
            store.item7()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="chillipowder":
        d=re.search(word,txt)
        print(d)
        if d:
            store.item8()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="pepper":
        e=re.search(word,txt)
        print(e)
        if e:
            store.item9()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()
    elif word=="nuts":
        f=re.search(word,txt)
        print(f)
        if f:
            store.item10()
            p=input("if want to add another item(yes/no):")
            if p=="yes":
                fun()         
    
fun()
def emailsending():
    try:
        f=open("bill.txt","r")
        txt=f.read()
        recevier_mail="abin59853@gmail.com"
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("thila2978@gmail.com","xuvv lcpl rvui cwzb")
        message=(f"super market bill: {txt}")
        s.sendmail("thila2978@gmail.com",recevier_mail,message)
        s.quit()
        print("mail send sucessfully")

    except:
        print("mail not send")
emailsending()


     

date=datetime.datetime.now()
print(date)
