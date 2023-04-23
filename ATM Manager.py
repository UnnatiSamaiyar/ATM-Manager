#*************** ATM MANAGER ****************"
import mysql.connector
# GLOBAL VARIABLES DECLARATION
myConnnection =""
cursor=""
cid=""
#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck ():
    global myConnection
    myConnection=mysql.connector.connect(host="localhost",user='root',password='yess', charset='utf8')
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor=myConnection.cursor()
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION")
#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection ():
    global myConnection
    myConnection=mysql.connector.connect(host="localhost",user='root',password='yess', database="ATM" , charset='utf8')
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()
# MODULE TO CREATE NEW CUSTOMER
def newCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        print("\nPlease Fill All The Information Carefully !")
        cid=input("Please Enter Customer ID : ")
        cname=input("Please Enter Customer Name : ")
        address=input("Please Enter Customer Address : ")
        phone=input("Please Enter Customer Contact No. : ")
        sql='INSERT INTO CUSTOMER(cid,cname,address,phone) values(%s,%s,%s,%s)'
        values=(cid,cname,address,phone)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nNew Customer Added Successfully !")
# MODULE TO DISPLAY CUSTOMER INFORMATION :
def displayAllCustomer():
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("SELECT * FROM CUSTOMER")
        data = cursor.fetchall()
    if data:
        print("\n*****DETAILS OF ALL CUSTOMER*****")
        print(data)
    else:
        print("Sorry ! No Record Found , Please Try Again ! ")
# MODULE TO SEARCH A CUSTOMER
def searchCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("Please Enter Customer ID : ")
        sql="SELECT * FROM CUSTOMER WHERE CID = %s"
        values=(cid,)
        data=cursor.execute(sql,values)
        data = cursor.fetchall()
    if data:
        print("\n*****CUSTOMER DETAILS*****")
        print(data)
    else:
        print("Sorry ! Customer NOT Found , Please Try Again ! ")
# MODULE TO OPEN A NEW ACCOUNT
def newAccount():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("Please Enter Customer ID : ")
        sql="SELECT * FROM CUSTOMER WHERE CID = %s"
        values=(cid,)
        data=cursor.execute(sql,values)
        data = cursor.fetchall()
    if data:
        account_no=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
        account_type=input("PLEASE ENTER THE ACCOUNT TYPE [ S-SAVING / C - CURRENT : ")
        amount=int(input("PLEASE ENTER THE AMOUNT TO DEPOSIT : "))
        ATM_pin=int(input("PLEASE ENTER THE ATM PIN [ FOUR DIGITIS ONLY ] : "))
        sql='INSERT INTO ACCOUNT (cid,account_no,account_type,amount ,pin) VALUES (%s,%s,%s,%s,%s)'
        values1=(cid,account_no,account_type,amount,ATM_pin)
        cursor.execute(sql,values1)
        cursor.execute("COMMIT")
        print("\nNew Account Opend Successfully !")
    else:
        print("Sorry ! Customer NOT Found , Please Try Again ! ")
# MODULE TO DISPLAY ALL ACCOUNTS
def displayAllAccounts():
    if myConnection:
         cursor=myConnection.cursor()
         cursor.execute("SELECT * FROM ACCOUNT")
         data = cursor.fetchall()
    if data:
         print("\n*****DETAILS OF ALL CUSTOMER*****")
         print(data)
    else:
         print("Sorry ! No Account Information , Please Try Again ! ")
# MODULE TO SEARCH AN ACCOUNT
def searchAccount():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("PLEASE ENTER CUSTOMER ID : ")
        account_no=int(input("PLEASE ENTER THE ACCOUNT NUMBER [0-9]: "))
        sql="SELECT * FROM ACCOUNT WHERE CID = %s AND ACCOUNT_NO =%s"
        values=(cid,account_no)
        data=cursor.execute(sql,values)
        data = cursor.fetchall()
    if data:
        print("\n*****CUSTOMER ACCOUNT DETAILS*****")
        print(data)
    else:
        print("Sorry ! Account Infromation NOT Found , Please Try Again ! ")
#MODULE TO PROVIDE HELP FOR USER
def helpMe():
    print("Please, Visit The Offcial Website Of ATM To Download The Mannual !!!")
#STARTING POINT OF THE SYSTEM
myConnection = MYSQLconnectionCheck ()
if myConnection:
    MYSQLconnection ()
    while(1):
        print("\n!=========================*************=======================!")
        print("! PLEASE ENTER 1 FOR NEW USER !")
        print("! PLEASE ENTER 2 TO DISPLAY ALL CUSTOMERS !")
        print("! PLEASE ENTER 3 TO SEARCH A CUSTOMER !")
        print("! PLEASE ENTER 4 TO OPEN NEW ACCOUNT !")
        print("! PLEASE ENTER 5 TO DISPLAY ALL ACCOUNTS !")
        print("! PLEASE ENTER 6 TO SEARCH AN ACCOUNT !")
        print("! PLEASE ENTER 7 TO EXIT !")
        print("! PLEASE ENTER 0 FOR HELP !")
        print("\n!============================*****END*****====================!")
        choice = int(input("\n Please Enter Your Choice : "))
        if choice == 1:
            newCustomer()
        elif choice == 2:
            displayAllCustomer()
        elif choice == 3:
            searchCustomer()
        elif choice == 4:
            newAccount()
        elif choice==5:
            displayAllAccounts()
        elif choice==6:
            searchAccount()
        elif choice==7:
            break
        elif choice==0:
            helpMe()
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("Check Your MYSQL Connection First !!! ")
#(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#(" TTTTT H H A N N K K ")
#(" T H H A A N N N K K ")
#(" T HHHHH A A A N N N K K Y Y OOOO U U ")
#(" T H H A A N N N K K Y Y O O U U ")
#(" T H H A A N N K K Y O O U U ")
#(" Y O O U U ")
#(" Y OOOO UUUU ")
#(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")



