import configparser #https://docs.python.org/3/library/configparser.html
import globales

def createConfig():
    config = configparser.ConfigParser()
    config['GENERAL'] = {'Username': globales.username,
                        'NumberOfSharedAccount' : 1}

    config['Account/' + globales.currentAccount] = {}
    accountConfig = config['Account/' + globales.currentAccount]
    accountConfig['Currency'] = globales.currentCurrency
    accountConfig['fichier'] = './' + globales.currentAccount.replace(" ", "_") + '.csv'

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def addAccount():
    config = configparser.ConfigParser()
    config.read('config.ini')

    nb = config.getint('GENERAL', 'NumberOfSharedAccount')
    config.set('GENERAL', 'NumberOfSharedAccount', str(nb+1))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    config['Account/' + globales.currentAccount] = {}
    accountConfig = config['Account/' + globales.currentAccount]
    accountConfig['Currency'] = globales.currentCurrency
    accountConfig['fichier'] = './' + globales.currentAccount.replace(" ", "_") + '.csv'
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def isConfigCreated():
    result = False

    config = configparser.ConfigParser()
    result = bool(config.read('config.ini'))
    return result

def getCSVFilePath(account):
    config = configparser.ConfigParser()
    config.read('config.ini')

    filepath = config.get('Account/' + account, 'fichier')
    return filepath