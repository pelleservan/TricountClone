import configparser #https://docs.python.org/3/library/configparser.html
import globales

def createConfig():
    config = configparser.ConfigParser()
    config['GENERAL'] = {'Username': globales.username,
                        'NumberOfSharedAccount' : len(globales.accountList)}

    for account in globales.accountList:
        i = 0
        config['Account/' + account] = {}
        globales.currentAccount = account
        accountConfig = config['Account/' + account]
        accountConfig['Currency'] = globales.currencyList[i]
        accountConfig['fichier'] = './' + account.replace(" ", "_") + '.csv'
        i+=1

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def addAccount():
    config = configparser.ConfigParser()
    config.read('config.ini')

    nb = config.getint('GENERAL', 'NumberOfSharedAccount')
    config.set('GENERAL', 'NumberOfSharedAccount', str(nb+1))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    for account in globales.accountList:
        i = 0
        config['Account/' + account] = {}
        accountConfig = config['Account/' + account]
        accountConfig['Currency'] = globales.currencyList[i]
        accountConfig['fichier'] = './' + account.replace(" ", "_") + '.csv'
        i+=1
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def isConfigCreated():
    result = False

    config = configparser.ConfigParser()
    result = bool(config.read('config.ini'))
    print(result)
    return result

def getCSVFilePath(account):
    config = configparser.ConfigParser()
    config.read('config.ini')

    filepath = config.get('Account/' + account, 'fichier')
    return filepath