from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile
import os
import EmployeeDatabase
# we have imported employee DB file, which is our backend, i am going to write that file now


# THIS IS OUR FRONTEND
class Employee:
    #__init__ is constructor in python
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Database Management System")

        # here +0+0 means that the window will open in left up corner
        self.root.geometry("1350x800+0+0")
        # set background colour, gainsboro is grey
        # you can also use config imstead of configure
        self.root.configure(bg='gainsboro')
        MainFrame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=1340, height=50, relief=RIDGE)
        TopFrame1.grid(row=2, column=0)

        TopFrame2 = Frame(MainFrame, bd=7, width=1340, height=100, relief=RIDGE)
        TopFrame2.grid(row=1, column=0)

        TopFrame3 = Frame(MainFrame, bd=7, width=1340, height=500, relief=RIDGE)
        TopFrame3.grid(row=0, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400,
                          padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180,
                           padx=4, pady=4, bg="gainsboro", relief=RIDGE)
        LeftFrame1.pack(side=TOP)
        LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height=180,
                           padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame2.pack(side=TOP)

        LeftFrame2Left = Frame(LeftFrame2, bd=5, width=300, height=170,
                               padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame2Left.pack(side=LEFT)
        LeftFrame2Right = Frame(LeftFrame2, bd=5, width=300, height=170,
                                padx=2, bg="gainsboro", relief=RIDGE)
        LeftFrame2Right.pack(side=RIGHT)

        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400,
                            padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=310, height=300,
                             padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame1a.pack(side=TOP)

        RightFrame2 = Frame(TopFrame3, bd=5, width=300, height=400,
                            padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2.pack(side=RIGHT)
        RightFrame2a = Frame(RightFrame2, bd=5, width=280, height=50,
                             padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2a.pack(side=TOP)
        RightFrame2b = Frame(RightFrame2, bd=5, width=280, height=180,
                             padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2b.pack(side=TOP)
        RightFrame2c = Frame(RightFrame2, bd=5, width=280, height=100,
                             padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2c.pack(side=TOP)
        RightFrame2d = Frame(RightFrame2, bd=5, width=280, height=50,
                             padx=2, bg="gainsboro", relief=RIDGE)
        RightFrame2d.pack(side=TOP)

        #---------------------- FUNCTIONS---------------------------------
        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Reference.set("")
            CityWeighting.set("")
            Mobile.set("")
            BasicSalary.set("")
            OverTime.set("")
            GrossPay.set("")
            NetPay.set("")
            Tax.set("")
            Pension.set("")
            stdLoan.set("")
            NIPayment.set("")
            Deductions.set("")
            Gender.set("")
            Payday.set("")
            TaxPeriod.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            PensionablePay.set("")
            TaxCode.set("")
            OtherPaymentDue.set("0.00")
            self.txtReceipt.delete("1.0", END)
        # ------------------------------VARIABLES------------------------------

        global Ed
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Reference = StringVar()
        CityWeighting = IntVar()
        Mobile = StringVar()
        BasicSalary = IntVar()
        OverTime = StringVar()
        GrossPay = StringVar()
        NetPay = StringVar()
        Tax = StringVar()
        Pension = StringVar()
        stdLoan = StringVar()
        NIPayment = StringVar()
        Deductions = StringVar()
        Gender = StringVar()
        Payday = StringVar()
        TaxPeriod = StringVar()
        NINumber = StringVar()
        NICode = StringVar()
        TaxablePay = StringVar()
        PensionablePay = StringVar()
        OtherPaymentDue = StringVar()
        TaxCode = StringVar()

        CityWeighting.set("")
        BasicSalary.set("")
        OtherPaymentDue.set("0.00")

        # --------------------------RECEIPT-----------------------------------
        self.txtReceipt = Text(RightFrame1a, height=23, width=42, bd=10, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        # --------------------LABEL USED FOR HEADING----------------------------
        self.lblLabel = Label(TopFrame2, font=('arial', 10, 'bold'), padx=6, pady=2,
                              text="Reference\tFirstname\tSurname\tAddress\t\tGender\tMobile\tNI Number\tStudent Loan\t Tax\tPension\t  Deductions\tNet Pay\t\tGross pay")
        self.lblLabel.grid(row=0, column=0, columnspan=17)

        # ---------------------Listbox and Scrollbar----------Receipt----------
        scrollbar = Scrollbar(TopFrame2)
        scrollbar.grid(row=1, column=1, sticky='ns')

        lstEmployee = Listbox(TopFrame2, width=145, height=5, font=(
            'arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        lstEmployee.bind('<<ListboxSelect>>')
        lstEmployee.grid(row=1, column=0, padx=1, sticky='nsew')
        scrollbar.config(command=lstEmployee.xview)

        # ------------------------WIDGET----------------------------------------

        self.lblReference = Label(LeftFrame1, font=('arial', 12, 'bold'),
                                  text="Reference", bd=7, bg="gainsboro", anchor='w')
        self.lblReference.grid(row=0, column=0, sticky=W, padx=5)
        self.txtReference = Entry(LeftFrame1, font=('arial', 12, 'bold'),
                                  bd=5, width=60, justify='left', textvariable=Reference)
        self.txtReference.grid(row=0, column=1)

        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'),
                                  text="First Name", bd=7, bg="gainsboro", anchor='w')
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5)
        self.txtFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5,
                                  width=60, justify='left', textvariable=Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'),
                                text="Surname", bd=7, bg="gainsboro", anchor='w')
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'),
                                bd=5, width=60, justify='left', textvariable=Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'),
                                text="Address", bd=7, bg="gainsboro", anchor='w')
        self.lblAddress.grid(row=3, column=0, sticky=W, padx=5)
        self.txtAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'),
                                bd=5, width=60, justify='left', textvariable=Address)
        self.txtAddress.grid(row=3, column=1)

        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'),
                               text="Gender", bd=7, bg="gainsboro", anchor='w')
        self.lblGender.grid(row=4, column=0, sticky=W, padx=5)
        self.txtGender = Entry(LeftFrame1, font=('arial', 12, 'bold'),
                               bd=5, width=60, justify='left', textvariable=Gender)
        self.txtGender.grid(row=4, column=1)

        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'),
                               text="Mobile No.", bd=7, bg="gainsboro", anchor='w')
        self.lblMobile.grid(row=5, column=0, sticky=W, padx=5)
        self.txtMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'),
                               bd=5, width=60, justify='left', textvariable=Mobile)
        self.txtMobile.grid(row=5, column=1)

        # ---------------WIDGETS IN DOWN BOX-------------------------------------

        self.lblCityWeighting = Label(LeftFrame2Left, font=('arial', 12, 'bold'),
                                      text="City Weighting", bd=7, bg="gainsboro", anchor='e')
        self.lblCityWeighting.grid(row=0, column=0, sticky=W)
        self.txtCityWeighting = Entry(LeftFrame2Left, font=('arial', 12, 'bold'),
                                      bd=5, width=20, justify='left', textvariable=CityWeighting)
        self.txtCityWeighting.grid(row=0, column=1)

        self.lblBasicSalary = Label(LeftFrame2Left, font=('arial', 12, 'bold'),
                                    text="Basic Salary", bd=7, bg="gainsboro", anchor='e')
        self.lblBasicSalary.grid(row=1, column=0, sticky=W)
        self.txtBasicSalary = Entry(LeftFrame2Left, font=('arial', 12, 'bold'),
                                    bd=5, width=20, justify='left', textvariable=BasicSalary)
        self.txtBasicSalary.grid(row=1, column=1)

        self.lblOverTime = Label(LeftFrame2Left, font=('arial', 12, 'bold'),
                                 text="Over Time", bd=7, bg="gainsboro", anchor='e')
        self.lblOverTime.grid(row=2, column=0, sticky=W)
        self.txtOverTime = Entry(LeftFrame2Left, font=('arial', 12, 'bold'),
                                 bd=5, width=20, justify='left', textvariable=OverTime)
        self.txtOverTime.grid(row=2, column=1)

        self.lblOtherPaymentDue = Label(LeftFrame2Left, font=('arial', 12, 'bold'),
                                        text="Other Payment Due", bd=7, bg="gainsboro", anchor='e')
        self.lblOtherPaymentDue.grid(row=3, column=0, sticky=W)
        self.txtOtherPaymentDue = Entry(LeftFrame2Left, font=('arial', 12, 'bold'),
                                        bd=5, width=20, justify='left', textvariable=OtherPaymentDue)
        self.txtOtherPaymentDue.grid(row=3, column=1)


# ---------------------------------------------------------------------------------

        self.lblTax = Label(LeftFrame2Right, font=('arial', 12, 'bold'),
                            text="Tax", bd=7, bg="gainsboro", anchor='e')
        self.lblTax.grid(row=0, column=0, sticky=W)
        self.txtTax = Entry(LeftFrame2Right, font=('arial', 12, 'bold'),
                            bd=5, width=20, justify='left', textvariable=Tax)
        self.txtTax.grid(row=0, column=1)

        self.lblPension = Label(LeftFrame2Right, font=('arial', 12, 'bold'),
                                text="Pension", bd=7, bg="gainsboro", anchor='e')
        self.lblPension.grid(row=1, column=0, sticky=W)
        self.txtPension = Entry(LeftFrame2Right, font=('arial', 12, 'bold'),
                                bd=5, width=20, justify='left', textvariable=Pension)
        self.txtPension.grid(row=1, column=1)

        self.lblstdLoan = Label(LeftFrame2Right, font=('arial', 12, 'bold'),
                                text="Student Loan", bd=7, bg="gainsboro", anchor='e')
        self.lblstdLoan.grid(row=2, column=0, sticky=W)
        self.txtstdLoan = Entry(LeftFrame2Right, font=('arial', 12, 'bold'),
                                bd=5, width=20, justify='left', textvariable=stdLoan)
        self.txtstdLoan.grid(row=2, column=1)

        self.lblNIPayment = Label(LeftFrame2Right, font=('arial', 12, 'bold'),
                                  text="NI Payment", bd=7, bg="gainsboro", anchor='e')
        self.lblNIPayment.grid(row=3, column=0, sticky=W)
        self.txtNIPayment = Entry(LeftFrame2Right, font=('arial', 12, 'bold'),
                                  bd=5, width=20, justify='left', textvariable=NIPayment)
        self.txtNIPayment.grid(row=3, column=1)


# ------------------------------------------------------------------------------
        self.lblPayday = Label(RightFrame2a, font=('arial', 12, 'bold'),
                               text="Payday", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblPayday.grid(row=0, column=0, sticky=W)
        self.txtPayday = Entry(RightFrame2a, font=('arial', 12, 'bold'),
                               bd=5, width=20, justify='left', textvariable=Payday)
        self.txtPayday.grid(row=0, column=1)

        self.lblTaxPeriod = Label(RightFrame2b, font=('arial', 12, 'bold'),
                                  text="Tax Period", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblTaxPeriod.grid(row=0, column=0, sticky=W)
        self.txtTaxPeriod = Entry(RightFrame2b, font=('arial', 12, 'bold'),
                                  bd=5, width=17, justify='left', textvariable=TaxPeriod)
        self.txtTaxPeriod.grid(row=0, column=1)

        self.lblTaxCode = Label(RightFrame2b, font=('arial', 12, 'bold'),
                                text="Tax Code", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblTaxCode.grid(row=1, column=0, sticky=W)
        self.txtTaxCode = Entry(RightFrame2b, font=('arial', 12, 'bold'),
                                bd=5, width=17, justify='left', textvariable=TaxCode)
        self.txtTaxCode.grid(row=1, column=1)

        self.lblNINumber = Label(RightFrame2b, font=('arial', 12, 'bold'),
                                 text="NI Number", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblNINumber.grid(row=2, column=0, sticky=W)
        self.txtNINumber = Entry(RightFrame2b, font=('arial', 12, 'bold'),
                                 bd=5, width=17, justify='left', textvariable=NINumber)
        self.txtNINumber.grid(row=2, column=1)

        self.lblNICode = Label(RightFrame2b, font=('arial', 12, 'bold'),
                               text="NI Code", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblNICode.grid(row=3, column=0, sticky=W)
        self.txtNICode = Entry(RightFrame2b, font=('arial', 12, 'bold'),
                               bd=5, width=17, justify='left', textvariable=NICode)
        self.txtNICode.grid(row=3, column=1)

        self.lblTaxablePay = Label(RightFrame2c, font=('arial', 12, 'bold'),
                                   text="Taxable Pay", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblTaxablePay.grid(row=0, column=0, sticky=W)
        self.txtTaxablePay = Entry(RightFrame2c, font=('arial', 12, 'bold'),
                                   bd=5, width=12, justify='left', textvariable=TaxablePay)
        self.txtTaxablePay.grid(row=0, column=1)

        self.lblPensionablePay = Label(RightFrame2c, font=('arial', 12, 'bold'),
                                       text="Pensionable Pay", bd=7, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblPensionablePay.grid(row=1, column=0, sticky=W)
        self.txtPensionablePay = Entry(RightFrame2c, font=('arial', 12, 'bold'),
                                       bd=5, width=12, justify='left', textvariable=PensionablePay)
        self.txtPensionablePay.grid(row=1, column=1)

        self.lblNetPay = Label(RightFrame2d, font=('arial', 12, 'bold'),
                               text="Net Pay", bd=5, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblNetPay.grid(row=0, column=0, sticky=W)
        self.txtNetPay = Entry(RightFrame2d, font=('arial', 12, 'bold'),
                               bd=5, width=17, justify='left', textvariable=NetPay)
        self.txtNetPay.grid(row=0, column=1)

        self.lblGrossPay = Label(RightFrame2d, font=('arial', 12, 'bold'),
                                 text="Gross Pay", bd=5, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblGrossPay.grid(row=1, column=0, sticky=W)
        self.txtGrossPay = Entry(RightFrame2d, font=('arial', 12, 'bold'),
                                 bd=5, width=17, justify='left', textvariable=GrossPay)
        self.txtGrossPay.grid(row=1, column=1)

        self.lblDeductions = Label(RightFrame2d, font=('arial', 12, 'bold'),
                                   text="Deductions", bd=5, bg="gainsboro", anchor='w', justify=LEFT)
        self.lblDeductions.grid(row=2, column=0, sticky=W)
        self.txtDeductions = Entry(RightFrame2d, font=('arial', 12, 'bold'),
                                   bd=5, width=17, justify='left', textvariable=Deductions)
        self.txtDeductions.grid(row=2, column=1)

        # ---------------------------ADD BUTTONS-----------------------------------------

        self.btnAddNewTotal = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                     width=8, text="AddNew/Total").grid(row=0, column=0, padx=1)

        self.btnPrint = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                               width=8, text="Print").grid(row=0, column=1, padx=1)

        self.btnDisplay = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                 width=8, text="Display").grid(row=0, column=2, padx=1)

        self.btnUpdate = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                width=8, text="Update").grid(row=0, column=3, padx=1)

        self.btnDelete = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                width=8, text="Delete").grid(row=0, column=4, padx=1)

        self.btnSearch = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                                width=8, text="Search").grid(row=0, column=5, padx=1)

        self.btnReset = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                               width=8, text="Reset", command=Reset).grid(row=0, column=6, padx=1)

        self.btnExit = Button(TopFrame1, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), padx=24,
                              width=8, text="Exit").grid(row=0, column=7, padx=1)


if __name__ == '__main__':
    root = Tk()
    application = Employee(root)
    root.mainloop()
