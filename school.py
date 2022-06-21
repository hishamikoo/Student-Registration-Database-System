import mysql.connector
import datetime

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                             *********SCHOOL REGISTRATION*********")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
db=mysql.connector.connect(host="localhost",
                             user="root",
                             password="hikjik123")


mycursor=db.cursor()
mycursor.execute("create database if not exists school")
mycursor.execute("use school")

mycursor.execute("create table if not exists student(ID_NO varchar(10) primary key,Password varchar(12) not null, Name varchar(30),Nationality char(20),Mobile_No varchar(15),fees int(6))")
mycursor.execute("create table if not exists student_info(ID_NO varchar(10),fees int(6),DoP date ,ttype char(1),foreign key (ID_NO) references student(ID_NO))")
db.commit()
e = 'y'
while e == 'y' or e == 'Y':
    
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("  Press 1 to Register ID_NO")
    print("  Press 2 to Deposit fees")
    print("  Press 3 for Balance fees (if necessary)")
    print("  Press 4 to View your account")
    print("  Press 5 to Delete registration")
    print("  Press 6 to view all registered accounts")
    print("  Press 7 to Change account password")
    print("  Press 8 to Retreat")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    ch = input("\n  Enter your choice and press Enter : ")
    

# enter student info for registration
    if(ch == "1"):
      try:
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("\n                                                                   All information prompted are mandatory to be filled")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          ID_NO = input("  Enter ID_NO: ")
          Pass ="y"
          while Pass == "y":
              password = input("  Create a password: ")
              confirm = input("  confirm password: ")
              if password == confirm:
                  print("\n  Password set successfully")
                  Pass = "n"
              else:
                  print("\n  Passwords do not match, please re-enter")
                  Pass="y"
          Name = input("  Enter name(limit 35 characters): ")
          Nationality = input("  Enter Nationality: ")
          Mobile_No = input("  Enter mobile no.: ")
          fees = 0
          mycursor.execute("insert into student values('"+ID_NO+"','"+password+"','"+Name+"','"+Nationality+"','"+Mobile_No+"','"+str(fees)+"')")
          db.commit()
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("\n                                                                     Account is successfully registered!!!")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      except:
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
          print("\n                                                               ID_NO-(",ID_NO,")is already taken, please enter")
          print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        

# for paying registration fees or exam fees.
    elif(ch == "2"):
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        try:
            ID_NO = input("  Enter ID_NO: ")
            Password = input("\n  Enter your password: ")
            mycursor.execute("select password from student where ID_NO = '"+ID_NO+"'")
            for x in mycursor:
                for paswd in x:
                    print()
            if Password in paswd:
                dp = input("  Enter amount to be paid: ")
                ymd = 'y'
                while ymd == 'y' or ymd =='Y':
                    try:
                        DoP = input("  Enter date of payment (YYYY-MM-DD): ")
                        ttype = "d"
                        mycursor.execute("insert into student_info values('"+ID_NO+"','"+str(dp)+"','"+DoP+"','"+ttype+"')")
                        mycursor.execute("update student set fees=fees+'"+str(dp)+"' where ID_NO='"+ID_NO+"'")
                        db.commit()
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("\n                                                                        Fees has been paid successully")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        ymd = 'n'
                    except:
                        print("Enter the date in the given format (YYYY-MM-DD)")
            else:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\n                                                                            Enter valid password ")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        except:
            print("Incorrect ID_NO or password")

# to withdraw the fees paid before in case of discount offered by school.
    elif(ch == "3"):
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        try:
            ID_NO = input("  Enter ID_NO: ")
            Password = input("\n  Enter your password: ")
            mycursor.execute("select password from student where ID_NO = '"+ID_NO+"'")
            for x in mycursor:
                for paswd in x:
                    print()
            if Password in paswd:
                wd = input("  Enter amount to be withdrawn: ")
                ymd = 'y'
                while ymd == 'y' or ymd =='Y':
                    try:
                        DoP = input("  Enter date of transaction (YYYY-MM-DD): ")
                        ttype = "w"
                        mycursor.execute("insert into student_info values('"+ID_NO+"','"+str(wd)+"','"+DoP+"','"+ttype+"')")
                        mycursor.execute("update student set fees=fees-'"+str(wd)+"' where ID_NO='"+ID_NO+"'")
                        db.commit()
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("\n                                                                          Transaction Successfull")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        ymd = 'n'
                    except:
                        print("Enter the date in the given format (YYYY-MM-DD)")
            else:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\n                                                                          Enter a valid password ")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        except:
            print("Incorrect ID_NO or Password")

# display the student information.
    elif(ch == "4"):
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        try:
            ID_NO = input("  Enter ID_NO: ")
            mycursor.execute("select * from student where ID_NO='"+ID_NO+"'")
            for i in mycursor:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(i)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        except:
            print("  Incorrect ID_NO or Password")

# to delete registration in case the student makes error in entering data while registering
    elif(ch == "5"):
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        try:
            
            ID_NO = input("  Enter ID_NO: ")
            Password = input("\n  Enter your password: ")
            mycursor.execute("select password from student where ID_NO = '"+ID_NO+"'")
            for x in mycursor:
                for paswd in x:
                    print()
            if Password in paswd:
                mycursor.execute("select * from student where ID_NO='"+ID_NO+"'")
                print("\n")
                for i in mycursor:
                    print(i)
                    print("\n")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                                 Are you sure you want to delete account",ID_NO,"(y/n): ")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                confirm = input()
                if confirm == 'y' or confirm == 'Y':
                    mycursor.execute("delete from student_info where ID_NO='"+ID_NO+"'")
                    db.commit()
                    mycursor.execute("delete from student where ID_NO='"+ID_NO+"'")
                    db.commit()
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\n   Account deleted on",datetime.date.today())
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                else:
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("                                                                            Your account was not deleted.")
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("\n  Enter a valid password ")
        except:
            print("  Incorrect ID_NO or Password")
    
    elif(ch == "6"):
        mycursor.execute("select * from student")
        for x in mycursor:
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(x)
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    elif(ch == "7"):
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        try:
            ID_NO = input("  Enter ID_NO: ")
            Password = input("\n  Enter your password: ")
            mycursor.execute("select Password from student where ID_NO = '"+ID_NO+"'")
            for x in mycursor:
                for paswd in x:
                    print()               
                    if Password in paswd:
                        Pass ="y"
                        while Pass == "y":
                            newpassword = input("\n  Enter a new password: ")
                            connewpassword = input("\n  Confirm your password: ")
                            if newpassword == connewpassword:
                                mycursor.execute("update student set password='"+newpassword+"' where ID_NO='"+ID_NO+"'")
                                db.commit()
                                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                print("\n  Password succesfully changed. ")
                                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                Pass = 'n'
                            else:
                                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                print("\n                                                           Passwords do not match, please enter a new one.")
                                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                Pass = 'y'
                    else:
                        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("\n                                                                     Password entered was incorrect. ")
                        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        except:
            print("  Incorrect ID_NO or Password.")
    
    elif(ch == "8"):
        break
    
    else:
        print("\n                                                                                        invalid choice")
    e = input('\n                                                                                   Go to main menu (y/n) - ')