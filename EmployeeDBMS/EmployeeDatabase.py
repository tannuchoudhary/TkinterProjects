import sqlite3
# This is our Backend


def EmployeeData():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(id INTEGER PRIMARK KEY, Reference text, \
    Firstname text, Surname text, Address text, Gender text, Mobile text, NINumber text, \
    stdLoan text, Tax text, Pension text, Deductions text, NetPay text, GrossPay text)")
    con.commit()
    con.close()


def addEmployeeRec(Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Employee VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay))
    con.commit()
    con.close()


def ViewData():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()
    con.close()
    return Rows


def deleteRec(id):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("DELETE * FROM Employee WHERE id=?", (id,))
    rows = cur.fetchall()
    con.commit()
    con.close()


def SearchData(Reference="", Firstname="", Surname="", Address="", Gender="", Mobile="", NINumber="", stdLoan="", Tax="",
               Pension="", Deductions="", NetPay="", GrossPay=""):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM EMPLOYEE WHERE Reference=? OR Firstname=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? \
                OR NINumber=? OR stdLoan=? OR Tax=? OR Pension=? OR Deduction=? OR NetPay=? OR GrossPay=? ",
                (Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay, id))
    rows = cur.fetchall()
    con.close()
    return Rows


def dataUpdate(Reference="", Firstname="", Surname="", Address="", Gender="", Mobile="", NINumber="", stdLoan="", Tax="",
               Pension="", Deductions="", NetPay="", GrossPay=""):
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    cur.execute("UPDATE Employee SET Reference=? OR Firstname=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? \
                OR NINumber=? OR stdLoan=? OR Tax=? OR Pension=? OR Deduction=? OR NetPay=? OR GrossPay=? ",
                (Reference, Firstname, Surname, Address, Gender, Mobile, NINumber, stdLoan, Tax, Pension, Deductions, NetPay, GrossPay, id))
    con.close()
    return Rows

    EmployeeData()
