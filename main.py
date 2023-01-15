from tkinter import *
from datetime import date
import globales
import configFunction
import csvFunction
import Classes
import pdfManager

# initialise les var globales
globales.initialize()

# colors
color0 = '#323232'  # background (grey)
color1 = '#FFA500'  # font title (orange)
color2 = 'white'  # font text (white)
color3 = '#FF4C4C'  # font warning message (red)
color4 = '#27C400'  # green

# fonts
font0 = 'DIN Condensed'  # title
font1 = 'Futura'  # test

# declare the window
window = Tk()
# set window title
window.title("Tricount Clone")
# set window width and height
window.geometry('1366x768')
# set window background color
window.configure(bg=color0)


def createAccount():
    if mainFrame:
        mainFrame.pack_forget()
        globales.initialize()

        # page création 1
    createAccountOneFrame = Frame(window)
    createAccountOneFrame.config(bg=color0)

    headCreateAccountOneFrame = Frame(createAccountOneFrame)
    headCreateAccountOneFrame.config(bg=color0)

    Label(headCreateAccountOneFrame, text='Create an account 1/2', font=(font0, 50), fg=color1, bg=color0).grid(row=0,
                                                                                                                column=0,
                                                                                                                sticky='nw')
    Label(headCreateAccountOneFrame, text='Choose an explicit title and give more information in the description',
          font=(font0, 30), fg=color2, bg=color0).grid(row=1, column=0, sticky='nw')

    headCreateAccountOneFrame.pack(side=TOP, expand=True, fill=BOTH)

    middleCreateAccountOneFrame = Frame(createAccountOneFrame)
    middleCreateAccountOneFrame.config(bg=color0)

    title = 'none'
    Label(middleCreateAccountOneFrame, text='Title :', font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=0,
                                                                                                    sticky='nw')
    Entry(middleCreateAccountOneFrame, width=50).grid(row=0, column=1)
    Label(middleCreateAccountOneFrame, text='Please specify a title (max. 50 characters)', font=(font1, 10), fg=color2,
          bg=color0).grid(row=0, column=3, sticky='nw')

    userName = 'none'
    Label(middleCreateAccountOneFrame, text='Your name :', font=(font1, 15), fg=color2, bg=color0).grid(row=1, column=0,
                                                                                                        sticky='nw')
    name = Entry(middleCreateAccountOneFrame, width=50)
    if configFunction.isConfigCreated():
        configFunction.InitUser()
        userName = globales.username
        name.insert(0, userName)
        name.config(state='disabled')
    name.grid(row=1, column=1)
    Label(middleCreateAccountOneFrame, text='Specify your name (max. 12 characters)', font=(font1, 10), fg=color2,
          bg=color0).grid(row=1, column=3, sticky='nw')

    Label(middleCreateAccountOneFrame, text='Currency  :', font=(font1, 15), fg=color2, bg=color0).grid(row=2, column=0,
                                                                                                        sticky='nw')
    cu = Entry(middleCreateAccountOneFrame, width=50)
    cu.insert(0, "EUR")
    cu.grid(row=2, column=1)
    Label(middleCreateAccountOneFrame, text='(EUR, USD, CHF, ...)', font=(font1, 10), fg=color2, bg=color0).grid(row=2,
                                                                                                                 column=3,
                                                                                                                 sticky='nw')

    Label(middleCreateAccountOneFrame, text='Description  :', font=(font1, 15), fg=color2, bg=color0).grid(row=3,
                                                                                                           column=0,
                                                                                                           sticky='nw')
    Entry(middleCreateAccountOneFrame, width=50).grid(row=3, column=1)

    middleCreateAccountOneFrame.pack(side=TOP, expand=True, fill=BOTH)

    # page création 2
    createAccountTwoFrame = Frame(window)
    createAccountTwoFrame.config(bg=color0)

    headCreateAccountTwoFrame = Frame(createAccountTwoFrame)
    headCreateAccountTwoFrame.config(bg=color0)

    Label(headCreateAccountTwoFrame, text='Create an account 2/2', font=(font0, 50), fg=color1, bg=color0).grid(row=0,
                                                                                                                column=0,
                                                                                                                sticky='nw')
    Label(headCreateAccountTwoFrame, text='List the people involved in the accounts', font=(font0, 30), fg=color2,
          bg=color0).grid(row=1, column=0, sticky='nw')

    headCreateAccountTwoFrame.pack(side=TOP, expand=True, fill=X)

    middleCreateAccountTwoFrame = Frame(createAccountTwoFrame)
    middleCreateAccountTwoFrame.config(bg=color0)

    footerCreateAccountTwoFrame = Frame(createAccountTwoFrame)
    footerCreateAccountTwoFrame.config(bg=color0)

    def next():
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
                    # récup title account
                    if (not widget.get() or len(widget.get()) > 50) and r == 0:
                        c = 1
                        Label(middleCreateAccountOneFrame, text='Please specify a title (max. 50 characters)',
                              font=(font1, 10), fg=color3).grid(row=r, column=3, sticky='nw')
                    elif widget.get() and len(widget.get()) < 50 and r == 0:
                        title = widget.get()
                        globales.currentAccount = title
                    # récup username
                    if (not widget.get() or len(widget.get()) > 12) and r == 1:
                        c = 1
                        Label(middleCreateAccountOneFrame, text='Specify your name (max. 12 characters)',
                              font=(font1, 10), fg=color3).grid(row=r, column=3, sticky='nw')
                    elif widget.get() and len(widget.get()) < 12 and r == 1:
                        userName = widget.get()
                        globales.username = userName
                        globales.listeParticipant = [userName]
                    # récup currency account
                    if (not widget.get() or not (widget.get().upper() in availableCurrency)) and r == 2:
                        c = 1
                        Label(middleCreateAccountOneFrame, text='Please use available currency (EUR, USD, CHF)').grid(
                            row=r, column=3, sticky='nw')
                    elif widget.get() and widget.get().upper() in availableCurrency and r == 2:
                        currency = widget.get().upper()
                        globales.currentCurrency = currency
                    # récup description
                    if widget.get() and len(widget.get()) > 0 and r == 3:
                        globales.currentDescription = widget.get()

            if c == 0:
                createAccountOneFrame.pack_forget()
                upDate()
                createAccountTwoFrame.pack()

    def upDate():

        partcipantFrame = Frame(middleCreateAccountTwoFrame)
        partcipantFrame.config(bg=color0)
        Label(partcipantFrame, text=globales.username, font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=0,
                                                                                                    sticky='w')
        Label(partcipantFrame, text=' (this is your name)', font=(font1, 10), fg=color2, bg=color0).grid(row=0,
                                                                                                         column=1,
                                                                                                         sticky='w')
        partcipantFrame.grid(row=0, column=0, sticky='nw')

    Button(createAccountOneFrame, text='Continue', command=lambda: next()).pack()

    createAccountOneFrame.pack()

    # content set in upDate()

    def addParticipant():
        top = Toplevel(window)
        top.title("Tricount Clone - Add participant")

        headTop = Frame(top)
        headTop.config(bg=color0)

        Label(headTop, text='Add participant', font=(font0, 30), fg=color2, bg=color0).pack()

        headTop.pack(side=TOP, expand=True, fill=X)

        middleTop = Frame(top)
        middleTop.config(bg=color0)

        Label(middleTop, text='His name', font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=0, sticky='nw')
        Entry(middleTop).grid(row=0, column=1, sticky='nw')

        middleTop.pack(side=TOP, expand=True, fill=X)

        footerTop = Frame(top)
        footerTop.config(bg=color0)

        def saveNewParticipant():
            newParticipantName = StringVar()

            def displayNewParticipant():
                r = 0
                for widget in middleCreateAccountTwoFrame.winfo_children():
                    r += 1

                participantFrame = Frame(middleCreateAccountTwoFrame)
                participantFrame.config(bg=color0)
                Label(participantFrame, textvariable=newParticipantName, font=(font1, 15), fg=color2, bg=color0).grid(
                    row=r, column=0, sticky='nw')
                Button(participantFrame, text='Delete', command=lambda: deleteParticipant()).grid(row=r, column=1,
                                                                                                  sticky='ne')
                participantFrame.grid(row=r, column=0, sticky='nw')

                def deleteParticipant():
                    globales.listeParticipant.remove(newParticipantName.get())
                    participantFrame.destroy()

            for widget in middleTop.winfo_children():
                if isinstance(widget, Entry):
                    if len(widget.get()) > 0:
                        newParticipantName.set(widget.get())
                        globales.listeParticipant.append(widget.get())
                        top.destroy()
                        displayNewParticipant()
                    else:
                        Label(middleTop, text='Specify a name').grid(row=0, column=2, sticky='nw')

        def cancelNewParticipant():
            top.destroy()

        Button(footerTop, text='Ok', command=lambda: saveNewParticipant()).grid(row=0, column=0, sticky='nw')
        Button(footerTop, text='Cancel', command=lambda: cancelNewParticipant()).grid(row=0, column=1, sticky='nw')

        footerTop.pack(side=BOTTOM, expand=True, fill=X)

    middleCreateAccountTwoFrame.pack(side=TOP, expand=True, fill=X)

    Button(createAccountTwoFrame, text='Add participant', command=lambda: addParticipant()).pack(side=TOP)

    backYet = 0

    def back():
        global backYet

        createAccountTwoFrame.pack_forget()
        createAccountOneFrame.pack()

        backYet = 1

    def finish():
        upDateHead()
        createAccountTwoFrame.pack_forget()
        mainFrame.pack()

        if not configFunction.isConfigCreated():
            # Création du fichier de config la première fois et du csv
            configFunction.createConfig()
            accountName = globales.currentAccount.replace(" ", "_")
            csvFunction.createCSV(accountName, globales.listeParticipant)
        else:
            # Ajout du nouveau compte dans le fichier de config et creation du csv
            configFunction.addAccount()
            accountName = globales.currentAccount.replace(" ", "_")
            csvFunction.createCSV(accountName, globales.listeParticipant)

        displayExpensesFrame()

    Button(footerCreateAccountTwoFrame, text='Back', command=lambda: back()).grid(row=0, column=0, sticky='nw')
    Button(footerCreateAccountTwoFrame, text='Finish', command=lambda: finish()).grid(row=0, column=1, sticky='ne')

    footerCreateAccountTwoFrame.pack(side=BOTTOM, expand=True, fill=X)


isConfigCreated = configFunction.isConfigCreated()

if isConfigCreated:
    configFunction.InitConfig()

mainFrame = Frame(window)


def upDateHead():
    global headMainFrame

    for widget in headMainFrame.winfo_children():
        widget.pack_forget()

    titleFrame = Frame(headMainFrame, width=1366)
    titleFrame.config(bg=color0)
    Label(titleFrame, text="Comptes '" + str(globales.currentAccount) + "'", font=(font0, 50), fg=color1,
          bg=color0).grid(row=0, column=0, sticky='nw')
    titleFrame.pack(side=TOP, expand=True, fill=X)
    Label(headMainFrame, text='Created by ' + str(globales.username) + ', on ' + str(date.today()), font=(font0, 30),
          fg=color2, bg=color0).pack(side=LEFT, expand=True, fill=X)

    buttonHeadMainFrame = Frame(headMainFrame)
    buttonHeadMainFrame.config(bg=color0)

    Button(buttonHeadMainFrame, text='Print', command=lambda: pdfManager.editPDF(globales.currentAccount, globales.username), width=10).pack(side=LEFT, expand=True, fill=X)
    Button(buttonHeadMainFrame, text='Creat account', command=lambda: createAccount(), width=10).pack(side=LEFT,
                                                                                                      expand=True,
                                                                                                      fill=X)
    Button(buttonHeadMainFrame, text='Exit', command=lambda: window.destroy(), width=10).pack(side=RIGHT, expand=True,
                                                                                              fill=X)

    buttonHeadMainFrame.pack(side=RIGHT, expand=True, fill=X)


# init Main frame
headMainFrame = Frame(mainFrame, width=1366)
headMainFrame.config(bg=color0)

headMainFrame.pack(side=TOP, expand=True, fill=X)

middleMainFrame = Frame(mainFrame, width=1366)
middleMainFrame.config(bg=color0)

headMiddleMainFrame = Frame(middleMainFrame, width=1366)
headMiddleMainFrame.config(bg=color0)

contentMiddleMainFrame = Frame(middleMainFrame, width=1366)
contentMiddleMainFrame.config(bg=color0)

# Init onglet frame
expensesFrame = Frame(middleMainFrame, width=1366)
expensesFrame.config(bg=color0)
balanceFrame = Frame(middleMainFrame, width=1366)
balanceFrame.config(bg=color0)
settingFrame = Frame(middleMainFrame, width=1366)
settingFrame.config(bg=color0)

expenseButton = Button(headMiddleMainFrame, text='Expenses', command=lambda: displayExpensesFrame(), bg=color1)
expenseButton.pack(side=LEFT, expand=True, fill=X)
balanceButton = Button(headMiddleMainFrame, text='Balance', command=lambda: displayBalanceFrame())
balanceButton.pack(side=LEFT, expand=True, fill=X)
settingsButton = Button(headMiddleMainFrame, text='Settings', command=lambda: displaySettingFrame())
settingsButton.pack(side=RIGHT, expand=True, fill=X)

headMiddleMainFrame.pack(side=TOP, fill=X)


def clearFrame(inputFrame):
    for widget in inputFrame.winfo_children():
        widget.pack_forget()


def displayExpensesFrame():
    global expensesFrame
    global contentMiddleMainFrame

    expenseButton.configure(bg=color1)
    balanceButton.configure(bg='white')
    settingsButton.configure(bg='white')

    clearFrame(contentMiddleMainFrame)

    if expensesFrame:
        expensesFrame.pack_forget()
        expensesFrame = Frame(contentMiddleMainFrame, width=1366)
        expensesFrame.config(bg=color0)

    def upDateHeadExpeses():
        global headExpensesFrame

        Label(headExpensesFrame, text='List of expenses', font=(font1, 15), fg=color2, bg=color0).pack(side=LEFT)
        Label(headExpensesFrame, text='You are identified as ' + str(globales.username), font=(font1, 15), fg=color2,
              bg=color0).pack(side=RIGHT)

        headExpensesFrame.pack(side=TOP, expand=True, fill=X)

    global headExpensesFrame
    headExpensesFrame = Frame(expensesFrame, width=1366)
    headExpensesFrame.config(bg=color0)
    # Content set in upDateHeadExpeses()
    headExpensesFrame.pack(side=TOP, expand=True, fill=X)

    upDateHeadExpeses()

    middleExepensesFrame = Frame(expensesFrame, width=1366)
    middleExepensesFrame.config(bg=color0)

    Label(middleExepensesFrame, text='Who paid, how much and why ?', font=(font1, 15), fg=color2, bg=color0).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  sticky='nw')
    Label(middleExepensesFrame, text='When ?', font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=1,
                                                                                            sticky='nw')
    Label(middleExepensesFrame, text='Who does it concern ?', font=(font1, 15), fg=color2, bg=color0).grid(row=0,
                                                                                                           column=2,
                                                                                                           sticky='nw')
    Label(middleExepensesFrame, text='For you ?', font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=3,
                                                                                               sticky='nw')

    allExpense = csvFunction.getAllExpense(configFunction.getCSVFilePath(globales.currentAccount))
    r = 1
    for expense in allExpense:
        text = expense.getLibelle() + ' ' + str(
            expense.getCoutTotal()) + ' ' + globales.currentCurrency + ', paid by ' + expense.getPaidBy()
        Label(middleExepensesFrame, text=text, font=(font1, 15), fg=color2, bg=color0).grid(row=r, column=0,
                                                                                            sticky='nw')
        r += 1

    middleExepensesFrame.pack(side=TOP, expand=True, fill=X)

    footerExpensesFrame = Frame(expensesFrame, width=1366)
    footerExpensesFrame.config(bg=color0)

    Button(footerExpensesFrame, text='Add expense', command=lambda: addExpenses()).grid(row=0, column=0, sticky='nw')

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
        if not value.replace('.', '', 1).isdigit():
            entryCost.delete(len(value) - 1, 'end')

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
                costPerParticipant[i].set('Cost : ' + str(round(totalCost / nbParticipant, 2)))
            else:
                costPerParticipant[i].set('Cost : 0')

    top = Toplevel(window)
    top.title("Tricount Clone - Add Expenses")

    headTop = Frame(top)
    headTop.config(bg=color0)

    Label(headTop, text='Add Expenses', font=(font0, 30), fg=color2, bg=color0).pack()

    headTop.pack(side=TOP, expand=True, fill=X)

    middleTop = Frame(top)
    middleTop.config(bg=color0)

    Label(middleTop, text='Expenses name', font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=0, sticky='nw')
    Entry(middleTop, textvariable=nameResult).grid(row=0, column=1, sticky='nw')

    Label(middleTop, text='Total cost', font=(font1, 15), fg=color2, bg=color0).grid(row=1, column=0, sticky='nw')
    entryCost = Entry(middleTop, textvariable=costResult)
    entryCost.grid(row=1, column=1, sticky='nw')
    entryCost.bind('<KeyRelease>', check_numeric)

    Label(middleTop, text='Paid by : ', font=(font1, 15), fg=color2, bg=color0).grid(row=2, column=0, sticky='nw')
    OptionMenu(middleTop, participantResult, *globales.listeParticipant).grid(row=2, column=1, sticky='nw')

    participantResult.trace('w', lambda *args: afficherNom())

    r = 3
    for name in globales.listeParticipant:
        checkBoxresult = IntVar()
        checkBoxresult.set(1)
        checkBoxOutput.append(checkBoxresult)
        Checkbutton(middleTop, text=name, variable=checkBoxresult, command=updateCheckButton, font=(font1, 15),
                    fg=color2, bg=color0, selectcolor=color0).grid(row=r, column=0, sticky='nw')
        costPerParticipantResult = StringVar()

        costPerParticipantResult.set('Cost : 0')
        costPerParticipant.append(costPerParticipantResult)
        Label(middleTop, textvariable=costPerParticipantResult, font=(font1, 15), fg=color2, bg=color0).grid(row=r,
                                                                                                             column=1,
                                                                                                             sticky='nw')
        r += 1

    middleTop.pack(side=TOP, expand=True, fill=X)

    footerTop = Frame(top)
    footerTop.config(bg=color0)

    def saveNewExpenses():

        def calculateExpenseForCSV(expenseName):
            listeCoutParticipant = []
            csvPath = configFunction.getCSVFilePath(globales.currentAccount)
            for i in range(len(globales.listeParticipant)):
                coutParticipant = Classes.CoutParticipant(float(costPerParticipant[i].get()[7:]),
                                                          globales.listeParticipant[i])
                listeCoutParticipant.append(coutParticipant)

            csvFunction.addLineCSV(csvPath, expenseName, listeCoutParticipant, participantResult.get())

        if len(nameResult.get()) > 0 and (len(costResult.get()) > 0 and float(costResult.get()) > 0):
            top.destroy()
            calculateExpenseForCSV(nameResult.get())
            # pour refresh la liste des expenses
            displayExpensesFrame()
        else:
            if len(nameResult.get()) == 0:
                Label(middleTop, text='Specify a name', font=(font1, 10), fg=color3, bg=color0).grid(row=0, column=2,
                                                                                                     sticky='nw')
            if len(costResult.get()) == 0 or float(costResult.get()) < 0:
                Label(middleTop, text='Specify a cost', font=(font1, 10), fg=color3, bg=color0).grid(row=1, column=2,
                                                                                                     sticky='nw')

    def cancelNewExpenses():
        top.destroy()

    Button(footerTop, text='Ok', command=lambda: saveNewExpenses()).grid(row=0, column=0, sticky='nw')
    Button(footerTop, text='Cancel', command=lambda: cancelNewExpenses()).grid(row=0, column=1, sticky='nw')

    footerTop.pack(side=BOTTOM, expand=True, fill=X)


def displayBalanceFrame():
    global balanceFrame
    global contentMiddleMainFrame

    expenseButton.configure(bg='white')
    balanceButton.configure(bg=color1)
    settingsButton.configure(bg='white')

    clearFrame(contentMiddleMainFrame)

    if balanceFrame:
        balanceFrame.pack_forget()
        balanceFrame = Frame(contentMiddleMainFrame, width=1366)
        balanceFrame.config(bg=color0)

    def upDateHeadBalance():
        global headBalanceFrame

        Label(headBalanceFrame, text='The reds owe the greens', font=(font1, 15), fg=color2, bg=color0).pack(side=LEFT)
        Label(headBalanceFrame, text='You are identified as ' + str(globales.username), font=(font1, 15), fg=color2,
              bg=color0).pack(side=RIGHT)

        headBalanceFrame.pack(side=TOP, expand=True, fill=X)

    global headBalanceFrame
    headBalanceFrame = Frame(balanceFrame, width=1366)
    headBalanceFrame.config(bg=color0)
    # Content set in upDateHeadBalance()
    headBalanceFrame.pack(side=TOP)

    upDateHeadBalance()

    rightMiddleBalanceFrame = Frame(balanceFrame, width=1366)
    rightMiddleBalanceFrame.config(bg=color0)

    # a faire en fonction du compte
    Label(rightMiddleBalanceFrame, text='How to balance? ', font=(font1, 15), fg=color2, bg=color0).grid(row=0,
                                                                                                         column=0,
                                                                                                         sticky='nw')
    Label(rightMiddleBalanceFrame, text='No payment is required to balance the books !', font=(font1, 15), fg=color2,
          bg=color0).grid(row=1, column=0, sticky='nw')

    rightMiddleBalanceFrame.pack(side=RIGHT, expand=True, fill=X)

    leftMiddleBalanceFrame = Frame(balanceFrame, width=1366)
    leftMiddleBalanceFrame.config(bg=color0)

    participantTotalListe = csvFunction.getExpensePerParticipant(configFunction.getCSVFilePath(globales.currentAccount))

    isCsvEmpty = csvFunction.isCSVEmpty(configFunction.getCSVFilePath(globales.currentAccount))

    r = 0
    for participantTotal in participantTotalListe:
        if not isCsvEmpty:
            text = participantTotal.getNom() + ' : ' + str(participantTotal.getTotal()) + ' ' + globales.currentCurrency
            if participantTotal.getTotal() > 0:
                Label(leftMiddleBalanceFrame, text=text, font=(font1, 15), fg=color2, bg=color4).grid(row=r, column=0,
                                                                                                      sticky='nw')
            else:
                Label(leftMiddleBalanceFrame, text=text, font=(font1, 15), fg=color2, bg=color3).grid(row=r, column=0,
                                                                                                      sticky='nw')
        else:
            Label(leftMiddleBalanceFrame, text=participantTotal.getNom() + ' : 0 ' + globales.currentCurrency,
                  font=(font1, 15), fg=color2, bg=color0).grid(row=r, column=0, sticky='nw')
        r += 1

    leftMiddleBalanceFrame.pack(side=LEFT, expand=True, fill=X)

    balanceFrame.pack(side=TOP, expand=True, fill=X)

def displaySettingFrame():
    global settingFrame
    global contentMiddleMainFrame

    accountListeResult = StringVar()
    accountListeResult.set(globales.currentAccount)
    accountListe = configFunction.getAccountListe()

    expenseButton.configure(bg='white')
    balanceButton.configure(bg='white')
    settingsButton.configure(bg=color1)

    def updateAccount():
        index = accountListe.index(accountListeResult.get()) + 1
        configFunction.InitConfig(index)
        displayExpensesFrame()

    clearFrame(contentMiddleMainFrame)

    if settingFrame:
        settingFrame.pack_forget()
        settingFrame = Frame(contentMiddleMainFrame, width=1366)
        settingFrame.config(bg=color0)

    def upDateHeadSetting():
        global headSettingFrame

        Label(headSettingFrame, text='General information', font=(font1, 15), fg=color2, bg=color0).pack(side=LEFT)
        Label(headSettingFrame, text='You are identified as ' + str(globales.username), font=(font1, 15), fg=color2,
              bg=color0).pack(side=RIGHT)

        headSettingFrame.pack(side=TOP, expand=True, fill=X)

    global headSettingFrame
    headSettingFrame = Frame(settingFrame, width=1366)
    headSettingFrame.config(bg=color0)
    # Content set in upDateHeadExpeses()
    headSettingFrame.pack(side=TOP, expand=True, fill=X)

    upDateHeadSetting()

    middleSettingFrame = Frame(settingFrame, width=1366)
    middleSettingFrame.config(bg=color0)

    Label(middleSettingFrame, text='Title :', font=(font1, 15), fg=color2, bg=color0).grid(row=0, column=0, sticky='nw')
    ti = Entry(middleSettingFrame, width=50)
    ti.insert(0, globales.currentAccount)
    ti.grid(row=0, column=1, sticky='nw')

    Label(middleSettingFrame, text='Currency :', font=(font1, 15), fg=color2, bg=color0).grid(row=1, column=0,
                                                                                              sticky='nw')
    Label(middleSettingFrame, text=globales.currentCurrency, font=(font1, 15), fg=color2, bg=color0).grid(row=1,
                                                                                                          column=1,
                                                                                                          sticky='nw')

    Label(middleSettingFrame, text='Description :', font=(font1, 15), fg=color2, bg=color0).grid(row=2, column=0,
                                                                                                 sticky='nw')
    desc = Entry(middleSettingFrame, width=50)
    desc.insert(0, globales.currentDescription)
    desc.grid(row=2, column=1, sticky='nw')

    Label(middleSettingFrame, text='Groupe', font=(font1, 15), fg=color2, bg=color0).grid(row=3, column=0, sticky='nw')
    Button(middleSettingFrame, text='Add participant').grid(row=3, column=1, sticky='nw')

    Label(middleSettingFrame, text='Switch account', font=(font1, 15), fg=color2, bg=color0).grid(row=4, column=0,
                                                                                                  sticky='nw')
    OptionMenu(middleSettingFrame, accountListeResult, *accountListe).grid(row=5, column=0, sticky='nw')
    accountListeResult.trace('w', lambda *args: updateAccount())

    middleSettingFrame.pack(side=TOP, expand=True, fill=X)

    settingFrame.pack(expand=True, fill=X)


if not isConfigCreated:
    createAccount()
else:
    upDateHead()
    mainFrame.pack()
    displayExpensesFrame()

contentMiddleMainFrame.pack(side=TOP, expand=True, fill=X)

middleMainFrame.pack(side=TOP, expand=True, fill=X)

window.mainloop()
