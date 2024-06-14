import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Dineshck75@',database='Bank_management')


def openAccount():
    n=input("Enter your Name : ")
    ac=input("Enter your account number :")
    db=input("Enter the date of birth : ")
    add=input("Enter your address : ")
    cn=input("Enter your Mobile number : ")
    ob=int(input("Enter your opening Balance : "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1 = ("insert into acc_table Values (%s,%s,%s,%s,%s,%s)") #it is query of sql to insert data into database table
    #The six %s symbols represent where each piece of information from our Python code will be inserted into the database table.

    sql2=('insert into ammount values (%s,%s,%s)')
    x=mydb.cursor() #It allows the code to point to a specific location within the database (like a particular table) and perform operations on the data there.
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit() #The .commit() method tells the database to finalize the changes made through the current set of operations.
    print("Enter data successfully")
    main()

def depositeAmount():
    amount=input("enter the amount for your deposit : ")
    ac = input("Enter your account number :")
    a='select balance from ammount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data) #The .execute() method tells the cursor to take control and perform an action based on the information provided.
    result=x.fetchone() #The .fetchone() method tells the cursor to retrieve only the very next row of data from the result set.
    t=result[0]+amount
    sql=('update ammount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def withdrawAmount():
    amount=input("enter the amount for your deposit : ")
    ac = input("Enter your account number :")
    a='select balance from ammount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]- amount
    sql=('update ammount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def balanceEniquery():
    ac=input("enter the account Number : ")
    a='select * from ammount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance from account : ",ac,"is",result[-1])
    main()

def viewDetails():
    ac=input("enter the account Number : ")
    a='select * from ammount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()

def closeAccount():
    ac=input("enter the account number : ")
    sql1='delete from acc_table where AccNo=%s'
    sql2='delete from ammount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()

def main():
    print('''
    1.Open New Account
    2.Deposit Amount
    3.Withdraw Amount
    4.Balance Enquiry
    5.Display Customer Details
    6.Close An Account
    ''')

    choice=input("Enter your task you want to perform: ")
    if choice == '1':
        openAccount()

    elif choice == '2':
        depositeAmount()

    elif choice == '3':
        withdrawAmount()

    elif choice == '4':
        balanceEniquery()

    elif choice == '5':
        viewDetails()

    elif choice == '6':
        closeAccount()

    else:
        print("invalid")
        main()


main()