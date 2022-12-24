from tkinter import *
from datetime import date
import globales
import configFunction

# initialise les var globales
globales.initialize() 

# declare the window
window = Tk()
# set window title
window.title("Tricount Clone")
# set window width and height
window.geometry('800x400')
# set window background color
window.configure(bg='white')

createAccountOneFrame = Frame(window)

headCreateAccountOneFrame = Frame(createAccountOneFrame)

Label(headCreateAccountOneFrame, text='Create an account 1/2').grid(row=0, column=0, sticky='nw')
Label(headCreateAccountOneFrame, text='Choose an explicit title and give more information in the description').grid(row=1, column=0, sticky='nw')

headCreateAccountOneFrame.pack(side=TOP, expand=True, fill=X)

middleCreateAccountOneFrame = Frame(createAccountOneFrame)

title = 'none'
Label(middleCreateAccountOneFrame, text='Title :').grid(row=0, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame).grid(row=0, column=1)

userName = 'none'
Label(middleCreateAccountOneFrame, text='Your name :').grid(row=1, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame).grid(row=1, column=1)

Label(middleCreateAccountOneFrame, text='Currency  :').grid(row=2, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame).grid(row=2, column=1)
Label(middleCreateAccountOneFrame, text='(EUR, USD, CHF, ...)').grid(row=2, column=3, sticky='nw')

Label(middleCreateAccountOneFrame, text='Description  :').grid(row=3, column=0, sticky='nw')
Entry(middleCreateAccountOneFrame).grid(row=3, column=1)

middleCreateAccountOneFrame.pack(side=TOP, expand=True, fill=X)

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
                    Label(middleCreateAccountOneFrame, text='Please specify a title (max. 50 characters)').grid(row=r, column=3, sticky='nw')
                elif widget.get() and len(widget.get()) < 50 and r == 0:
                    title = widget.get()
                    globales.accountList = [title]
                #récup username
                if (not widget.get() or len(widget.get()) > 12 ) and r == 1:
                    c = 1
                    Label(middleCreateAccountOneFrame, text='Specify your name (max. 12 characters)').grid(row=r, column=3, sticky='nw')
                elif widget.get() and len(widget.get()) < 12 and r == 1:
                    userName = widget.get()
                    globales.username = userName
                #récup currency account
                if (not widget.get() or widget.get() in availableCurrency ) and r == 2:
                    c = 1
                    Label(middleCreateAccountOneFrame, text='Please use available currency (EUR, USD, CHF)').grid(row=r, column=3, sticky='nw')
                elif widget.get() and widget.get() in availableCurrency and r == 2:
                    currency = widget.get()
                    print(widget.get())
                    print('test') # marche pas 
                    globales.currencyList = [currency]

        if c == 0:
            createAccountOneFrame.pack_forget()
            upDate()
            createAccountTwoFrame.pack()

def upDate():
    global UserName # c'est pas en trop ça ?

    partcipantFrame = Frame(middleCreateAccountTwoFrame)
    Label(partcipantFrame, text=userName).grid(row=0, column=0, sticky='nw')
    Label(partcipantFrame, text=' (this is your name)').grid(row=0, column=1, sticky='nw')
    partcipantFrame.grid(row=0, column=0, sticky='nw')

Button(createAccountOneFrame, text='Continue', command=lambda:next()).pack()

footerCreateAccountOneFrame.pack(side=BOTTOM, expand=True, fill=X)

createAccountOneFrame.pack()

createAccountTwoFrame = Frame(window)

headCreateAccountTwoFrame = Frame(createAccountTwoFrame)

Label(headCreateAccountTwoFrame, text='Create an account 2/2').grid(row=0, column=0, sticky='nw')
Label(headCreateAccountTwoFrame, text='List the people involved in the accounts').grid(row=1, column=0, sticky='nw')

headCreateAccountTwoFrame.pack(side=TOP, expand=True, fill=X)

middleCreateAccountTwoFrame = Frame(createAccountTwoFrame)

#content set in upDate()

def addParticipant():
    top = Toplevel(window)
    top.title("Tricount Clone - Add participant")

    headTop = Frame(top)

    Label(headTop, text='Add participant').pack()

    headTop.pack(side=TOP, expand=True, fill=X)

    middleTop = Frame(top)

    Label(middleTop, text='His name').grid(row=0, column=0, sticky='nw')
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
            Label(participantFrame, text=newParticipantName).grid(row=r, column=0, sticky='nw')
            Button(participantFrame, text='Delete', command=lambda:participantFrame.destroy()).grid(row=r, column=1, sticky='ne')
            participantFrame.grid(row=r, column=0, sticky='nw')

            footerCreateAccountTwoFrame.pack_forget()
            footerCreateAccountTwoFrame = Frame(createAccountTwoFrame)
            Button(footerCreateAccountTwoFrame, text='Finish').pack()
            footerCreateAccountTwoFrame.pack(side=BOTTOM, expand=True, fill=X)

        for widget in middleTop.winfo_children():
            if isinstance(widget, Entry):
                if len(widget.get()) > 0:
                    newParticipantName = widget.get()
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

    configFunction.createConfig()

Button(footerCreateAccountTwoFrame, text='Back', command=lambda:back()).grid(row=0, column=0, sticky='nw')
Button(footerCreateAccountTwoFrame, text='Finish', command=lambda:finish()).grid(row=0, column=1, sticky='ne')

footerCreateAccountTwoFrame.pack(side=BOTTOM, expand=True, fill=X)

mainFrame = Frame(window)

def upDateHead():
    global headMainFrame

    for widget in headMainFrame.winfo_children():
        widget.pack_forget()

    Label(headMainFrame, text="Comptes '"+str(title)+"'").grid(row=0, column=0, sticky='nw')
    Label(headMainFrame, text='Created by '+str(userName)+', on '+str(date.today())).grid(row=1, column=0, sticky='nw')

    buttonHeadMainFrame = Frame(headMainFrame)

    Button(buttonHeadMainFrame, text='Print').grid(row=0, column=0, sticky='nw')
    Button(buttonHeadMainFrame, text='Creat account').grid(row=0, column=1, sticky='nw')
    Button(buttonHeadMainFrame, text='Exit').grid(row=0, column=2, sticky='nw')

    buttonHeadMainFrame.grid(row=1, column=1, sticky='ne')

headMainFrame = Frame(mainFrame)

headMainFrame.pack(side=TOP)

middleMainFrame = Frame(mainFrame)

headMiddleMainFrame = Frame(middleMainFrame)

Button(headMiddleMainFrame, text='Expenses', command=lambda:displayExpensesFrame()).grid(row=0, column=0, sticky='nw')
Button(headMiddleMainFrame, text='Balance', command=lambda:displayBalanceFrame()).grid(row=0, column=1, sticky='nw')
Button(headMiddleMainFrame, text='Share', command=lambda:displayShareFrame()).grid(row=0, column=2, sticky='nw')
Button(headMiddleMainFrame, text='Settings', command=lambda:displaySettingFrame()).grid(row=0, column=3, sticky='nw')

headMiddleMainFrame.pack(side=TOP)

def clearFrame(inputFrame):
    for widget in inputFrame.winfo_children():
        widget.pack_forget()

def displayExpensesFrame():
    global expensesFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if expensesFrame :
        expensesFrame.pack_forget()
        expensesFrame = Frame(contentMiddleMainFrame)

    def upDateHeadExpeses():
        global headExpensesFrame

        Label(headExpensesFrame, text='List of expenses').grid(row=0, column=0, sticky='nw')
        Label(headExpensesFrame, text='You are identified as '+str(userName)).grid(row=0, column=1, sticky='nw')

        headExpensesFrame.pack(side=TOP)

    global headExpensesFrame
    headExpensesFrame = Frame(expensesFrame)
    #Content set in upDateHeadExpeses()
    headExpensesFrame.pack(side=TOP)

    upDateHeadExpeses()

    middleExepensesFrame = Frame(expensesFrame)

    Label(middleExepensesFrame, text='Who paid, how much and why ?').grid(row=0, column=0, sticky='nw')
    Label(middleExepensesFrame, text='When ?').grid(row=0, column=1, sticky='nw')
    Label(middleExepensesFrame, text='Who does it concern ?').grid(row=0, column=2, sticky='nw')
    Label(middleExepensesFrame, text='For you ?').grid(row=0, column=3, sticky='nw')

    middleExepensesFrame.pack(side=TOP)

    footerExpensesFrame = Frame(expensesFrame)

    Button(footerExpensesFrame, text='Add expense').grid(row=0, column=0, sticky='nw')

    footerExpensesFrame.pack(side=BOTTOM)

    expensesFrame.pack()

def displayBalanceFrame():
    global balanceFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if balanceFrame:
        balanceFrame.pack_forget()
        balanceFrame = Frame(contentMiddleMainFrame)

    def upDateHeadBalance():
        global headBalanceFrame

        Label(headBalanceFrame, text='The reds owe the greens').grid(row=0, column=0, sticky='nw')
        Label(headBalanceFrame, text='You are identified as '+str(userName)).grid(row=0, column=1, sticky='nw')

        headBalanceFrame.pack(side=TOP)

    global headBalanceFrame
    headBalanceFrame = Frame(balanceFrame)
    #Content set in upDateHeadBalance()
    headBalanceFrame.pack(side=TOP)

    upDateHeadBalance()

    rightMiddleBalanceFrame = Frame(balanceFrame)

    #a faire en fonction du compte
    Label(rightMiddleBalanceFrame, text='How to balance? ').grid(row=0, column=0, sticky='nw')
    Label(rightMiddleBalanceFrame, text='No payment is required to balance the books !').grid(row=1, column=0, sticky='nw')

    rightMiddleBalanceFrame.pack(side=RIGHT)

    leftMiddleBalanceFrame = Frame(balanceFrame)

    #a faire en fonction du compte
    Label(leftMiddleBalanceFrame, text='user').grid(row=0, column=0, sticky='nw')
    Label(leftMiddleBalanceFrame, text='user').grid(row=0, column=1, sticky='nw')
    Label(leftMiddleBalanceFrame, text='user').grid(row=0, column=2, sticky='nw')

    leftMiddleBalanceFrame.pack(side=LEFT)

    balanceFrame.pack(side=TOP)

def displayShareFrame():
    global shareFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if shareFrame :
        shareFrame.pack_forget()
        shareFrame = Frame(contentMiddleMainFrame)

    def upDateHeadShare():
        global headShareFrame

        Label(headShareFrame, text='Invite friends to participate in the accounts').grid(row=0, column=0, sticky='nw')
        Label(headShareFrame, text='You are identified as '+str(userName)).grid(row=0, column=1, sticky='nw')

        headShareFrame.pack(side=TOP)

    global headShareFrame
    headShareFrame = Frame(shareFrame)
    #Content set in upDateHeadExpeses()
    headShareFrame.pack(side=TOP)

    upDateHeadShare()

    middleShareFrame = Frame(shareFrame)

    Label(middleShareFrame, text='Copy the text below into an email and send it to the group :').pack(side=TOP)
    
    contentMiddleShareFrame = Frame(middleShareFrame)

    Label(contentMiddleShareFrame, text='The '+str(title)+' accounts are accessible on Tricount :').grid(row=0, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='To access :').grid(row=1, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='• From your mobile device, download the Tricount app (for iPhone, Android and Windows) and then follow the link :').grid(row=2, column=0, sticky='nw')
    Label(contentMiddleShareFrame, text='• From a computer, simply click on the link ').grid(row=1, column=0, sticky='nw')

    contentMiddleShareFrame.pack(side=TOP)

    middleShareFrame.pack(side=TOP)

    shareFrame.pack()

def displaySettingFrame():
    global settingFrame
    global contentMiddleMainFrame

    clearFrame(contentMiddleMainFrame)

    if settingFrame :
        settingFrame.pack_forget()
        settingFrame = Frame(contentMiddleMainFrame)

    def upDateHeadSetting():
        global headSettingFrame

        Label(headSettingFrame, text='General information').grid(row=0, column=0, sticky='nw')
        Label(headSettingFrame, text='You are identified as '+str(userName)).grid(row=0, column=1, sticky='nw')

        headSettingFrame.pack(side=TOP)

    global headSettingFrame
    headSettingFrame = Frame(shareFrame)
    #Content set in upDateHeadExpeses()
    headSettingFrame.pack(side=TOP)

    upDateHeadSetting()

    middleSettingFrame = Frame(settingFrame)

    Label(middleSettingFrame, text='A faire depuis un fichier').grid(row=0, column=0, sticky='nw')

    middleSettingFrame.pack(side=TOP)

    settingFrame.pack()

contentMiddleMainFrame = Frame(middleMainFrame)

expensesFrame = Frame(middleMainFrame)
balanceFrame = Frame(middleMainFrame)
shareFrame = Frame(middleMainFrame)
settingFrame = Frame(middleMainFrame)

contentMiddleMainFrame.pack(side=TOP)

middleMainFrame.pack(side=TOP)

window.mainloop()