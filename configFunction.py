import configparser #https://docs.python.org/3/library/configparser.html
import globales

def createConfig():
    config = configparser.ConfigParser()
    config['GENERAL'] = {'Username': globales.username,
                        'NumberOfSharedAccount' : len(globales.accountList)}

    for account in globales.accountList:
        i = 0
        config['Account/' + account] = {}
        accountConfig = config['Account/' + account]
        #accountConfig['Currency'] = globales.currencyList[i]
        accountConfig['fichier'] = './' + account + '.csv'
        i+=1

    with open('config.ini', 'w') as configfile:
        config.write(configfile)