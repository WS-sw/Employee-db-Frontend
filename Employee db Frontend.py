import sqlite3
from tkinter import *
import tkinter.messagebox

class Employee:

    def __init__(self,root):

        self.root = root
        self.root.title("Employee Data")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="white")

#Get values 
        Efirst_name= StringVar()
        Elast_name= StringVar()
        Edepartment= StringVar()
        Eaddress= StringVar()
        Ephone_number= StringVar()
        Epay= StringVar()

        '''Create the frame'''
        MainFrame = Frame(self.root,bg="CadetBlue1")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="CadetBlue1", relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.iTitle = Label(HeadFrame, font=('arial',50,'bold'), fg='red', 
            text='Employee Data',bg='SkyBlue')
        self.iTitle.grid()

        OperationFrame = Frame(MainFrame,bd=2,width=1300,height=60,
            padx=30,pady=20,bg='SkyBlue', relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame,bd=2,width=1300,height=400,
            padx=30,pady=20,bg='SkyBlue', relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame,bd=2,width= 600, height= 230,
            padx=20,pady=10,bg='CadetBlue1',relief=RIDGE, font=('arial',15,'bold'),
                    text='Employee Details:')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd=2,width= 300, height= 230,
            padx=20,pady=10,bg='CadetBlue1',relief=RIDGE, font=('arial',15,'bold'),
                    text='Employee Details:')
        LeftBodyFrame.pack(side=LEFT)
        
        '''Add Widgets to LeftBodyFrame'''

        self.labelEFIRST_NAME=Label(LeftBodyFrame, font=('arial',15,'bold'),
            text= "First name :", padx=2, bg='white', fg='CadetBlue1')
        self.labelEFIRST_NAME.grid(row=0, column=1,sticky=W)
        self.txteID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
            textvariable=Efirst_name, width=35)
        self.txteID.grid(row=0, column=1,sticky=W)

        self.labelELAST_NAME = Label(LeftBodyFrame, font=('arial',15,'bold'),
            text= "Last name :", padx=2, bg='white', fg='CadetBlue1')
        self.labelELAST_NAME.grid(row=1, column=1,sticky=W)
        self.txteID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
            textvariable=Elast_name, width=35)
        self.txteID.grid(row=1, column=1,sticky=W)

        self.labelEDEPARTMENT = Label(LeftBodyFrame, font=('arial',20,'bold'),
            text= "Department :", padx=2, bg='white', fg='CadetBlue1')
        self.labelEDEPARTMENT.grid(row=2, column=2,sticky=W)
        self.txteID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
            textvariable=Edepartment, width=35)
        self.txteID.grid(row=2, column=1,sticky=W)

        self.labelEADDRESS = Label(LeftBodyFrame, font=('arial',20,'bold'),
            text= "Address :", padx=2, bg='white', fg='CadetBlue1')
        self.labelEADDRESS.grid(row=3, column=3,sticky=W)
        self.txteID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
            textvariable=Eaddress, width=35)
        self.txteID.grid(row=3, column=1,sticky=W)

        self.labelEPHONE = Label(LeftBodyFrame, font=('arial',20,'bold'),
            text= "Phone", padx=2, bg='white', fg='CadetBlue1')
        self.labelEPHONE.grid(row=0, column=1,sticky=W)
        self.txteID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
            textvariable=Ephone_number, width=35)
        self.txteID.grid(row=4, column=1,sticky=W)

        self.labelEPAY = Label(LeftBodyFrame, font=('arial',20,'bold'),
            text= "Pay", padx=2, bg='white', fg='CadetBlue1')
        self.labelEPAY.grid(row=0, column=1,sticky=W)
        self.txteID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
            textvariable=Epay, width=35)
        self.txteID.grid(row=5, column=1,sticky=W)


        ''' Add Scroll bar '''
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column = 1,sticky='ns')

        employeeList=Listbox(RightBodyFrame, width=40, height=16, 
            font=('arial', 12, 'bold'),yscrollcommand=scroll.set)

        employeeList.grid(row=0, column=0, padx=8)
        scroll.config(command=employeeList.yview)

        ''' Add operation Frame buttons '''
        self.buttonSaveData = Button(OperationFrame, text='Save',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonSaveData.grid(row = 0, column=1)

        self.buttonShowData = Button(OperationFrame, text='Show Data',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonShowData.grid(row = 0, column=2)

        self.buttonDelete = Button(OperationFrame, text='Delete',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonDelete.grid(row = 0, column=3)

        self.buttonClear = Button(OperationFrame, text='Clear',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonClear.grid(row = 0, column=4)

        self.buttonSearch = Button(OperationFrame, text='Search',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonSearch.grid(row = 0, column=5)

        self.buttonUpdate = Button(OperationFrame, text='Update',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonUpdate.grid(row = 0, column=6)

        self.buttonClose = Button(OperationFrame, text='Close',
            font=('arial', 18, 'bold'), height=2,width='10',bd=4)
        self.buttonClose.grid(row = 0, column=7)
    

if __name__ =='__main__':
    root=Tk()
    application = Employee(root)
    root.mainloop()