

def OpenAccount():
    name = input("Enter The Name: ")
    accountNo = input("Enter The Account No: ")
    dob = input("Enter The Date Of Birth: ")
    address = input("Enter The Address: ")
    contactNo = input("Enter The Contact Number: ")
    openingBalance =  int(input("Enter The Opening Balance: "))

    data1 = (name,accountNo,dob,address,contactNo,openingBalance)
    data2 = (name,accountNo,openingBalance)

    sql1 = ('INSERT INTO account VALUES(%s,%s,%s,%s,%s,%s)')

    sql2 = ('INSERT INTO amount VALUES (%s,%s,%s)')

