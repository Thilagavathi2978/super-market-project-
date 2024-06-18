
def item1():
    print("rice is avaiable")
    try:
        how_many=int(input("enter a  howmany(kg):"))
        one_kg=90
        print("price:90")
        rate=one_kg*how_many
        print(f"total price : {rate}")
        f=open("bill.txt","a")
        f.write(f"\n{how_many} kg rice :{rate}")
    
    except :
        print("pls enter in number")

def item2():
    print("oil is avaiable")
    try:
        how_many=int(input("enter a  howmany(litre):"))
        one_lt=150
        print("price:150")
        ol=one_lt*how_many
        print(f"total price : {ol}")
        f=open("bill.txt","a")
        f.write(f"\n{how_many} liter oil: {ol}")
    except:
        print("pls enter  in number")

def item3():
     print("sugar is avaiable")
     try:
        how_many=int(input("enter a  howmany(kg):"))
        one_su=190
        print("price:190")
        su=one_su*how_many
        print(f"total price : {su}")
        f=open("bill.txt","a")
        f.write(f"\nsugar: {su}")
     except:
         print("pls enter in number")

def item4():
    print("flour is avaiable")
    try:
        how_many=int(input("enter a howmany(kg):"))
        one_kg=80
        print("price:80")
        flour=one_kg*how_many
        print(f"total price :{flour}")
        f=open("bill.txt","a")
        f.write(f"\n {how_many}kg flour: {flour}")
    except:
        print("pls entern in numbers")

def item5():
    print("dal is avaiable")
    try:
        how_many=int(input("enter a howmany(kg):"))
        one_kg=100
        print("price:100")
        dal=one_kg*how_many
        print(f" total price: {dal}")
        f=open("bill.txt","a")
        f.write(f"\n{how_many} kg dal: {dal}")
    except:
        print("pls enter in number")

def item6():
    list=["lux","chandrika","medimix"]
    print(f"soap varities:{list}")
    y=input("enter your soap:")
    if y in list:
       if y=="lux":
           how_many=int(input("enter a howmany soap:"))
           one_soap=70
           print(f"one_piece:{one_soap}")
           soap=one_soap*how_many
           print(f"total price of soap :{soap}") 
           f=open("bill.txt","a")
           f.write(f"\n{how_many} pcs lux soap: {soap}")        
       elif y=="chandrika":
           how_many=int(input("enter a howmany soap:"))
           one_soap= 80
           print(f"one_piece:{one_soap}")
           soap=one_soap*how_many
           print(f"total price of soap : {soap}")
           f=open("bill.txt","a")
           f.write(f"\n{how_many} pcs chadrika soap: {soap}")
       elif y=="medimix":
           how_many=int(input("enter a howmany soap:"))
           one_soap= 60
           print(f"one_piece:{one_soap}")
           soap=one_soap*how_many
           print(f"total price of soap : {soap}")
           f=open("bill.txt","a")
           f.write(f"\n{how_many}pcs medimix soap: {soap}")
def item7():
    print("butter is avaiable")
    try:
        how_many=int(input("enter a  howmany(gram):"))
        one_gr=190
        print("price:190")
        bu=one_gr*how_many
        print(f"total price of butter: {bu}")
        f=open("bill.txt","a")
        f.write(f"\n{how_many} kg butter: {bu}")
    except:
        print("pls enter in numbers")

def item8():
    print(" chilli powder is avaiable")
    try:
        how_many=int(input("enter a  howmany(pack):"))
        one_lt=40
        print("one pacK:40")
        chilli=one_lt*how_many
        print(f"total price :{chilli}")
        f=open("bill.txt","a")
        f.write(f"\n{how_many}pack chilli powder:{chilli}")
    except:
        print("pls enter in numbers")

def item9():
    print("pepper is avaiable")
    try:
        how_many=int(input("enter a  howmany(gram):"))
        one_pack=80
        print("price :40")
        pe=one_pack*how_many
        print(f"total price :{pe}")
        f=open("bill.txt","a")
        f.write(f"\n{how_many}kg pepper: {pe}")
    except:
        print("pls enter in numbers")
def item10():
    print("nuts : cashew , badam, pista") 
    lst=["cashew","badam","pista"]
    r=input("enter a nuts:")
    if r in lst:
        if r=="cashew":
            how_many=int(input("enter a  howmany(kg):"))
            one_pack=200
            print("price:200")
            cashew=one_pack*how_many
            print(f"total price :{cashew}")
            f=open("bill.txt","a")
            f.write(f"\n{how_many}kg cashew: {cashew}")
        elif r=="badam":
            how_many=int(input("enter a  howmany(kg):"))
            one_pack=350
            print("price:350")
            badam=one_pack*how_many
            print(f"total price badam :{badam}")
            f=open("bill.txt","a")
            f.write(f"\n{how_many}kg badam: {badam}")
        elif r=="pista":
            how_many=int(input("enter a  howmany(kg):"))
            one_pack=500
            print("price:500")
            pista=one_pack*how_many
            print(f"total price :{pista}")
            f=open("bill.txt","a")
            f.write(f"\n{how_many}kg pista: {pista}")
   