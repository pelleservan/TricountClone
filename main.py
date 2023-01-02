from tkinter import *
from datetime import date
import globales
import configFunction
import csvFunction
import Classes

# initialise les var globales
globales.initialize() 

isConfigCreated = configFunction.isConfigCreated()

#colors
color0 = '#323232' #background (grey)
color1 = '#FFA500' #font title (orange)
color2 = 'white' #font text (white)
color3 = '#FF4C4C' #font warning message (red)

#fonts
font0 = 'DIN Condensed' #title
font1 = 'Futura' #test

# declare the window
window = Tk()
# set window title
window.title("Tricount Clone")
# set window width and height
window.geometry('800x400')
# set window background color
window.configure(bg=color0)

createAccountOneFrame = Frame(window)

headCreateAccountOneFrame = Frame(createAccountOneFrame)

Label(headCreateAccountOneFrame, text='Create an account 1/2', font=(font0, 50), fg=color1).grid(row=0, column=0, sticky='nw')
Label(headCreateAccountOneFrame, text='Choose an explicit title and give more information in the description', font=(font0, 30), fg=color2).grid(row=1, column=0, sticky='nw')

headCreateAccountOneFrame.pack(side=TOP, expand=True, fill=BOTH)

middleCreateAccountOneFrame = Frame(createAccountOneFrame)

title = 'none'
Label(middleCreateAccountOneFrame, text='Title :', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame, width=50).grid(row=0, column=1)
Label(middleCreateAccountOneFrame, text='Please specify a title (max. 50 characters)', font=(font1, 10), fg=color0).grid(row=0, column=3, sticky='nw')

userName = 'none'
Label(middleCreateAccountOneFrame, text='Your name :', font=(font1, 15), fg=color2).grid(row=1, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame, width=50).grid(row=1, column=1)
Label(middleCreateAccountOneFrame, text='Specify your name (max. 12 characters)', font=(font1, 10), fg=color0).grid(row=1, column=3, sticky='nw')

Label(middleCreateAccountOneFrame, text='Currency  :', font=(font1, 15), fg=color2).grid(row=2, column=0, sticky='nw')
cu = Entry(middleCreateAccountOneFrame, width=50)
cu.insert(0, "EUR")
cu.grid(row=2, column=1)
Label(middleCreateAccountOneFrame, text='(EUR, USD, CHF, ...)', font=(font1, 10), fg=color2).grid(row=2, column=3, sticky='nw')

Label(middleCreateAccountOneFrame, text='Description  :', font=(font1, 15), fg=color2).grid(row=3, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame, width=50).grid(row=3, column=1)

middleCreateAccountOneFrame.pack(side=TOP, expand=True, fill=BOTH)

footerCreateAccountOneFrame = Frame(createAccountOneFrame)

def next():
    global createAccountOneFrame
    global createAccountTwoFrame
    global userName
    global title
    global currency
    availableCurrency = ['EUR', 'USD', 'CHF']

    if backYet == 1:
        createAccountOneFrame.pack_forget()
        createAccountTwoFrame.pack()

    elif backYet == 0:

        c = 0
        r = -1
        for widget in middleCreateAccountOneFrame.winfo_children():
            if isinstance(widget, Entry):
                r += 1
                #récup title account
                if (not widget.get() or len(widget.get()) > 50 ) and r == 0:
                    c = 1
                    Label(middleCreateAccountOneFrame, text='Please specify a title (max. 50 characters)', font=(font1, 10), fg=color3).grid(row=r, column=3, sticky='nw')
                elif widget.get() and len(widget.get()) < 50 and r == 0:
                    title = widget.get()
                    globales.currentAccount = title
                #récup username
                if (not widget.get() or len(widget.get()) > 12 ) and r == 1:
                    c = 1
                    Label(middleCreateAccountOneFrame, text='Specify your name (max. 12 characters)', font=(font1, 10), fg=color3).grid(row=r, column=3, sticky='nw')
                elif widget.get() and len(widget.get()) < 12 and r == 1:
                    userName = widget.get()
                    globales.username = userName
                    globales.listeParticipant = [userName]
                #récup currency account
                if (not widget.get() or not (widget.get().upper() in availableCurrency) ) and r == 2:
                    c = 1
                    Label(middleCreateAccountOneFrame, text='Please use available currency (EUR, USD, CHF)').grid(row=r, column=3, sticky='nw')
                elif widget.get() and widget.get().upper() in availableCurrency and r == 2:
                    currency = widget.get().upper()
                    globales.currentCurrency = currency

        if c == 0:
            createAccountOneFrame.pack_forget()
            upDate()
            createAccountTwoFrame.pack()

def upDate():
    global UserName # c'est pas en trop ça ?

    partcipantFrame = Frame(middleCreateAccountTwoFrame)
    Label(partcipantFrame, text=userName, font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='w')
    Label(partcipantFrame, text=' (this is your name)', font=(font1, 10), fg=color2).grid(row=0, column=1, sticky='w')
    partcipantFrame.grid(row=0, column=0, sticky='nw')

Button(createAccountOneFrame, text='Continue', command=lambda:next()).pack()

footerCreateAccountOneFrame.pack(side=BOTTOM, expand=True, fill=BOTH)

createAccountOneFrame.pack()

createAccountTwoFrame = Frame(window)

headCreateAccountTwoFrame = Frame(createAccountTwoFrame)

Label(headCreateAccountTwoFrame, text='Create an account 2/2', font=(font0, 50), fg=color1).grid(row=0, column=0, sticky='nw')
Label(headCreateAccountTwoFrame, text='List the people involved in the accounts', font=(font0, 30), fg=color2).grid(row=1, column=0, sticky='nw')

headCreateAccountTwoFrame.pack(side=TOP, expand=True, fill=X)

middleCreateAccountTwoFrame = Frame(createAccountTwoFrame)

#content set in upDate()

def addParticipant():
    top = Toplevel(window)
    top.title("Tricount Clone - Add participant")

    headTop = Frame(top)

    Label(headTop, text='Add participant', font=(font0, 30), fg=color2).pack()

    headTop.pack(side=TOP, expand=True, fill=X)

    middleTop = Frame(top)

    Label(middleTop, text='His name', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    Entry(middleTop).grid(row=0, column=1, sticky='nw')

    middleTop.pack(side=TOP, expand=True, fill=X)

    footerTop = Frame(top)

    def saveNewParticipant():
        global newParticipantName
        global footerCreateAccountTwoFrame
        global middleCreateAccountTwoFrame

        def displayNewParticipant():
            r=0
            for widget in middleCreateAccountTwoFrame.winfo_children():
                r += 1

            participantFrame  = Frame(middleCreateAccountTwoFrame)
            Label(participantFrame, text=newParticipantName, font=(font1, 15), fg=color2).grid(row=r, column=0, sticky='nw')
            Button(participantFrame, text='Delete', command=lambda:participantFrame.destroy()).grid(row=r, column=1, sticky='ne')
            participantFrame.grid(row=r, column=0, sticky='nw')

            footerCreateAccountTwoFrame.pack_forget() # il y a une erreur ici
            footerCreateAccountTwoFrame = Frame(createAccountTwoFrame)
            Button(footerCreateAccountTwoFrame, text='Finish').pack()
            footerCreateAccountTwoFrame.pack(side=BOTTOM, expand=True, fill=X)

        for widget in middleTop.winfo_children():
            if isinstance(widget, Entry):
                if len(widget.get()) > 0:
                    newParticipantName = widget.get()
                    globales.listeParticipant.append(widget.get())
                    top.destroy()
                    displayNewParticipant()
                else:
                    Label(middleTop, text='Specify a name').grid(row=0, column=2, sticky='nw')
                    

    def cancelNewParticipant():
        top.destroy()

    Button(footerTop, text='Ok', command=lambda:saveNewParticipant()).grid(row=0, column=0, sticky='nw')
    Button(footerTop, text='Cancel', command=lambda:cancelNewParticipant()).grid(row=0, column=1, sticky='nw')

    footerTop.pack(side=BOTTOM, expand=True, fill=X)

middleCreateAccountTwoFrame.pack(side=TOP, expand=True, fill=X)

Button(createAccountTwoFrame, text='Add participant', command=lambda:addParticipant()).pack(side=TOP)

footerCreateAccountTwoFrame = Frame(createAccountTwoFrame)

backYet = 0

def back():
    global backYet

    createAccountTwoFrame.pack_forget()
    createAccountOneFrame.pack()

    backYet = 1

def deleteParticipent():
    for widget in middleCreateAccountTwoFrame.winfo_children():
        if isinstance(widget, Button):
            if widget['state'] == 'normal':
                widget.pack_forget()

def finish():
    upDateHead()
    createAccountTwoFrame.pack_forget()
    mainFrame.pack()
    displayExpensesFrame()

    # Création du fichier de config la première fois et du csv
    configFunction.createConfig()
    accountName = title.replace(" ", "_")
    csvFunction.createCSV(accountName, globales.listeParticipant)

    # test ajout d'autre compte
    # globales.currentAccount = ['Voyage']
    # globales.currentCurrency = ['EUR']
    # configFunction.addAccount()

Button(footerCreateAccountTwoFrame, text='Back', command=lambda:back()).grid(row=0, column=0, sticky='nw')
Button(footerCreateAccountTwoFrame, text='Finish', command=lambda:finish()).grid(row=0, column=1, sticky='ne')

footerCreateAccountTwoFrame.pack(side=BOTTOM, expand=True, fill=X)

mainFrame = Frame(window)

def upDateHead():
    global headMainFrame

    for widget in headMainFrame.winfo_children():
        widget.pack_forget()

    titleFrame = Frame(headMainFrame, width=800)
    Label(titleFrame, text="Comptes '"+str(title)+"'", font=(font0, 50), fg=color1).grid(row=0, column=0, sticky='nw')
    titleFrame.pack(side=TOP, expand=True, fill=X)
    Label(headMainFrame, text='Created by '+str(userName)+', on '+str(date.today()), font=(font0, 30), fg=color2).pack(side=LEFT, expand=True, fill=X)

    buttonHeadMainFrame = Frame(headMainFrame)

    Button(buttonHeadMainFrame, text='Print', width=10).pack(side=LEFT, expand=True, fill=X)
    Button(buttonHeadMainFrame, text='Creat account', width=10).pack(side=LEFT, expand=True, fill=X)
    Button(buttonHeadMainFrame, text='Exit', command=lambda:window.destroy(), width=10).pack(side=RIGHT, expand=True, fill=X)

    buttonHeadMainFrame.pack(side=RIGHT, expand=True, fill=X)

headMainFrame = Frame(mainFrame, width=800)

headMainFrame.pack(side=TOP, expand=True, fill=X)

middleMainFrame = Frame(mainFrame, width=800)

headMiddleMainFrame = Frame(middleMainFrame, width=800)

Button(headMiddleMainFrame, text='Expenses', command=lambda:displayExpensesFrame(), bg=color1).pack(side=LEFT, expand=True, fill=X)
Button(headMiddleMainFrame, text='Balance', command=lambda:displayBalanceFrame()).pack(side=LEFT, expand=True, fill=X)
Button(headMiddleMainFrame, text='Share', command=lambda:displayShareFrame()).pack(side=LEFT, expand=True, fill=X)
Button(headMiddleMainFrame, text='Settings', command=lambda:displaySettingFrame()).pack(side=RIGHT, expand=True, fill=X)

headMiddleMainFrame.pack(side=TOP, fill=X)

def clearFrame(inputFrame):
    for widget in inputFrame.winfo_children():
        widget.pack_forget()

def displayExpensesFrame():
    global expensesFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if expensesFrame :
        expensesFrame.pack_forget()
        expensesFrame = Frame(contentMiddleMainFrame, width=800)

    def upDateHeadExpeses():
        global headExpensesFrame

        Label(headExpensesFrame, text='List of expenses', font=(font1, 15), fg=color2).pack(side=LEFT)
        Label(headExpensesFrame, text='You are identified as '+str(userName), font=(font1, 15), fg=color2).pack(side=RIGHT)

        headExpensesFrame.pack(side=TOP, expand=True, fill=X)

    global headExpensesFrame
    headExpensesFrame = Frame(expensesFrame, width=800)
    #Content set in upDateHeadExpeses()
    headExpensesFrame.pack(side=TOP, expand=True, fill=X)

    upDateHeadExpeses()

    middleExepensesFrame = Frame(expensesFrame, width=800)

    Label(middleExepensesFrame, text='Who paid, how much and why ?', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    Label(middleExepensesFrame, text='When ?', font=(font1, 15), fg=color2).grid(row=0, column=1, sticky='nw')
    Label(middleExepensesFrame, text='Who does it concern ?', font=(font1, 15), fg=color2).grid(row=0, column=2, sticky='nw')
    Label(middleExepensesFrame, text='For you ?', font=(font1, 15), fg=color2).grid(row=0, column=3, sticky='nw')

    middleExepensesFrame.pack(side=TOP, expand=True, fill=X)

    footerExpensesFrame = Frame(expensesFrame, width=800)

    Button(footerExpensesFrame, text='Add expense', command=lambda:addExpenses()).grid(row=0, column=0, sticky='nw')

    footerExpensesFrame.pack(side=BOTTOM, expand=True, fill=X)

    expensesFrame.pack(expand=True, fill=X)

def addExpenses():
    participantResult = StringVar()
    participantResult.set(globales.listeParticipant[0])
    nameResult = StringVar()
    costResult = StringVar()
    checkBoxOutput = []
    costPerParticipant = []

    def check_numeric(event):
        value = entryCost.get()
        if not value.replace('.','',1).isdigit():
            entryCost.delete(len(value)-1, 'end')

        updateCostPerParticipant()
    
    def updateCheckButton():
        updateCostPerParticipant()

    def afficherNom():
        updateCostPerParticipant()

    def updateCostPerParticipant():
        nbParticipant = 0
        for checkBoxResult in checkBoxOutput:
            if checkBoxResult.get() == 1:
                nbParticipant += 1
        if costResult.get():
            totalCost = float(costResult.get())
        else:
            totalCost = float(0)
        for i in range(len(checkBoxOutput)):
            if checkBoxOutput[i].get() == 1:
                costPerParticipant[i].set('Cost : ' + str(totalCost/nbParticipant))
            else:
                costPerParticipant[i].set('Cost : 0')

    
    top = Toplevel(window)
    top.title("Tricount Clone - Add Expenses")

    headTop = Frame(top)

    Label(headTop, text='Add Expenses', font=(font0, 30), fg=color2).pack()

    headTop.pack(side=TOP, expand=True, fill=X)

    middleTop = Frame(top)

    Label(middleTop, text='Expenses name', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    Entry(middleTop, textvariable=nameResult).grid(row=0, column=1, sticky='nw')

    Label(middleTop, text='Total cost', font=(font1, 15), fg=color2).grid(row=1, column=0, sticky='nw')
    entryCost = Entry(middleTop, textvariable=costResult)
    entryCost.grid(row=1, column=1, sticky='nw')
    entryCost.bind('<KeyRelease>', check_numeric)
    
    Label(middleTop, text='Paid by : ', font=(font1, 15), fg=color2).grid(row=2, column=0, sticky='nw')
    OptionMenu(middleTop, participantResult, *globales.listeParticipant).grid(row=2, column=1, sticky='nw')

    participantResult.trace('w', lambda *args: afficherNom())

    r=3
    for name in globales.listeParticipant:
        checkBoxresult = IntVar()
        checkBoxresult.set(1)
        checkBoxOutput.append(checkBoxresult)
        Checkbutton(middleTop, text=name, variable=checkBoxresult, command=updateCheckButton).grid(row=r, column=0, sticky='nw')
        costPerParticipantResult = StringVar()
        costPerParticipantResult.set('Cost : 0')
        costPerParticipant.append(costPerParticipantResult)
        Label(middleTop, textvariable=costPerParticipantResult, font=(font1, 15), fg=color2).grid(row=r, column=1, sticky='nw')
        r+=1

    
    middleTop.pack(side=TOP, expand=True, fill=X)

    footerTop = Frame(top)

    def saveNewExpenses():

        def calculateExpenseForCSV(expenseName):
            listeCoutParticipant = []
            csvPath = configFunction.getCSVFilePath(globales.currentAccount)
            for i in range(len(globales.listeParticipant)):
                coutParticipant = Classes.CoutParticipant(float(costPerParticipant[i].get()[7:]), globales.listeParticipant[i])
                listeCoutParticipant.append(coutParticipant)
                
            csvFunction.addLineCSV(csvPath, expenseName, listeCoutParticipant, participantResult.get())


        if len(nameResult.get()) > 0 and (len(costResult.get()) > 0 and float(costResult.get()) > 0):
            top.destroy()
            calculateExpenseForCSV(nameResult.get())
        else:
            if len(nameResult.get()) == 0:
                Label(middleTop, text='Specify a name', font=(font1, 10), fg=color3).grid(row=0, column=2, sticky='nw')
            if len(costResult.get()) == 0 or float(costResult.get()) < 0:
                Label(middleTop, text='Specify a cost', font=(font1, 10), fg=color3).grid(row=1, column=2, sticky='nw')

    def cancelNewExpenses():
        top.destroy()

    Button(footerTop, text='Ok', command=lambda:saveNewExpenses()).grid(row=0, column=0, sticky='nw')
    Button(footerTop, text='Cancel', command=lambda:cancelNewExpenses()).grid(row=0, column=1, sticky='nw')

    footerTop.pack(side=BOTTOM, expand=True, fill=X)

def displayBalanceFrame():
    global balanceFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if balanceFrame:
        balanceFrame.pack_forget()
        balanceFrame = Frame(contentMiddleMainFrame, width=800)

    def upDateHeadBalance():
        global headBalanceFrame

        Label(headBalanceFrame, text='The reds owe the greens', font=(font1, 15), fg=color2).pack(side=LEFT)
        Label(headBalanceFrame, text='You are identified as '+str(userName), font=(font1, 15), fg=color2).pack(side=RIGHT)

        headBalanceFrame.pack(side=TOP, expand=True, fill=X)

    global headBalanceFrame
    headBalanceFrame = Frame(balanceFrame, width=800)
    #Content set in upDateHeadBalance()
    headBalanceFrame.pack(side=TOP)

    upDateHeadBalance()

    rightMiddleBalanceFrame = Frame(balanceFrame, width=800)

    #a faire en fonction du compte
    Label(rightMiddleBalanceFrame, text='How to balance? ', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    Label(rightMiddleBalanceFrame, text='No payment is required to balance the books !', font=(font1, 15), fg=color2).grid(row=1, column=0, sticky='nw')

    rightMiddleBalanceFrame.pack(side=RIGHT, expand=True, fill=X)

    leftMiddleBalanceFrame = Frame(balanceFrame, width=800)

    #a faire en fonction du compte
    Label(leftMiddleBalanceFrame, text='user', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    Label(leftMiddleBalanceFrame, text='user', font=(font1, 15), fg=color2).grid(row=0, column=1, sticky='nw')
    Label(leftMiddleBalanceFrame, text='user', font=(font1, 15), fg=color2).grid(row=0, column=2, sticky='nw')

    leftMiddleBalanceFrame.pack(side=LEFT, expand=True, fill=X)

    balanceFrame.pack(side=TOP, expand=True, fill=X)

def displayShareFrame():
    global shareFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if shareFrame :
        shareFrame.pack_forget()
        shareFrame = Frame(contentMiddleMainFrame, width=800)

    def upDateHeadShare():
        global headShareFrame

        Label(headShareFrame, text='Invite friends to participate in the accounts', font=(font1, 15), fg=color2).pack(side=LEFT)
        Label(headShareFrame, text='You are identified as '+str(userName), font=(font1, 15), fg=color2).pack(side=RIGHT)

        headShareFrame.pack(side=TOP, expand=True, fill=X)

    global headShareFrame
    headShareFrame = Frame(shareFrame, width=800)
    #Content set in upDateHeadExpeses()
    headShareFrame.pack(side=TOP, expand=True, fill=X)

    upDateHeadShare()

    middleShareFrame = Frame(shareFrame, width=800)
    
    contentMiddleShareFrame = Frame(middleShareFrame, width=800)

    Label(contentMiddleShareFrame, text='Copy the text below into an email and send it to the group :', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='The '+str(title)+' accounts are accessible on Tricount :', font=(font1, 15), fg=color2).grid(row=1, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='To access :', font=(font1, 15), fg=color2).grid(row=2, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='• From your mobile device, download the Tricount app', font=(font1, 15), fg=color2).grid(row=3, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text=' (for iPhone, Android and Windows) and then follow the link :', font=(font1, 15), fg=color2).grid(row=4, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='• From a computer, simply click on the link ', font=(font1, 15), fg=color2).grid(row=5, column=0, sticky='nw')

    contentMiddleShareFrame.pack(side=TOP, expand=True, fill=X)

    middleShareFrame.pack(side=TOP, expand=True, fill=X)

    shareFrame.pack(expand=True, fill=X)

def displaySettingFrame():
    global settingFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if settingFrame :
        settingFrame.pack_forget()
        settingFrame = Frame(contentMiddleMainFrame, width=800)

    def upDateHeadSetting():
        global headSettingFrame

        Label(headSettingFrame, text='General information', font=(font1, 15), fg=color2).pack(side=LEFT)
        Label(headSettingFrame, text='You are identified as '+str(userName), font=(font1, 15), fg=color2).pack(side=RIGHT)

        headSettingFrame.pack(side=TOP, expand=True, fill=X)

    global headSettingFrame
    headSettingFrame = Frame(shareFrame, width=800)
    #Content set in upDateHeadExpeses()
    headSettingFrame.pack(side=TOP, expand=True, fill=X)

    upDateHeadSetting()

    middleSettingFrame = Frame(settingFrame, width=800)

    Label(middleSettingFrame, text='Title :', font=(font1, 15), fg=color2).grid(row=0, column=0, sticky='nw')
    ti = Entry(middleSettingFrame, width=50)
    ti.insert(0, title)
    ti.grid(row=0, column=1, sticky='nw')

    Label(middleSettingFrame, text='Currency :', font=(font1, 15), fg=color2).grid(row=1, column=0, sticky='nw')
    Label(middleSettingFrame, text='Euro ').grid(row=1, column=1, sticky='nw')

    Label(middleSettingFrame, text='Description :', font=(font1, 15), fg=color2).grid(row=2, column=0, sticky='nw')
    Entry(middleSettingFrame, width=50).grid(row=2, column=1, sticky='nw')

    Label(middleSettingFrame, text='Groupe', font=(font1, 15), fg=color2).grid(row=3, column=0, sticky='nw')
    Button(middleSettingFrame, text='Add participant').grid(row=3, column=1, sticky='nw')

    middleSettingFrame.pack(side=TOP, expand=True, fill=X)

    settingFrame.pack(expand=True, fill=X)

contentMiddleMainFrame = Frame(middleMainFrame, width=800)

expensesFrame = Frame(middleMainFrame, width=800)
balanceFrame = Frame(middleMainFrame, width=800)
shareFrame = Frame(middleMainFrame, width=800)
settingFrame = Frame(middleMainFrame, width=800)

contentMiddleMainFrame.pack(side=TOP, expand=True, fill=X)

middleMainFrame.pack(side=TOP, expand=True, fill=X)

window.mainloop()