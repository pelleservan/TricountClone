import globales
import Classes
import math
import pandas as pd

def createCSV(fileName, participants):

    header = ['LibelleDepense']
    header.append('nbParticipants')
    header.extend(participants)
    df = pd.DataFrame(columns=header)

    df.to_csv(fileName + '.csv', index=None, header=True)

def addLineCSV(fileName, expenseName, listCoutParticipant, paidBy):
    # Chargement le fichier CSV dans un DataFrame
    df = pd.read_csv(fileName)

    # Création d'une série vide avec les types de données souhaités
    empty_row = pd.Series(dtype='object')

    currentIndex = 0

    # vérif si le dataframe est vide
    if df.empty:
        # Création d'une nouvelle ligne
        df.loc[1] = empty_row
        currentIndex = 1

    else:
        # Récup de la dernière ligne du DataFrame
        last_row = df.index[-1]
        # Ajout d'une ligne vide juste après la dernière ligne
        df.loc[last_row+1] = empty_row
        currentIndex = last_row+1
    
    #récup nbr de participant
    nbParticipant = 0
    for coutParticipant in listCoutParticipant:
        if float(coutParticipant.getCout()) != 0:
            nbParticipant += 1

    # Ajout du libelle + nb participant
    newDf = pd.DataFrame(dtype=object)
    newDf.loc[currentIndex, 'LibelleDepense'] = expenseName
    newDf.loc[currentIndex, 'nbParticipants'] = nbParticipant

    for coutParticipant in listCoutParticipant:
        cout = 0
        if coutParticipant.getParticipant() == paidBy:
            if nbParticipant > 1:
                # calcul du cout
                cout = + (float(coutParticipant.getCout()) * (nbParticipant - 1))
            else:
                # calcul du cout
                cout = + float(coutParticipant.getCout())
        else:
            # calcul du cout
            cout = - float(coutParticipant.getCout())
            
        # Remplir les valeurs de la nouvelle ligne
        newDf.loc[currentIndex, coutParticipant.getParticipant()] = cout
    
    newDf.to_csv(fileName, mode='a', index=None, header=False)

def getAllExpense(fileName):
    # Chargement le fichier CSV dans un DataFrame
    df = pd.read_csv(fileName)

    resultExpenseListe = []

    for index, row in df.iterrows():
        nbParticipant = row[1]
        expense = Classes.Expense(row[0], 0, '') 
        i = 2
        for col in row[2:]:
            if float(col) > 0 and nbParticipant > 1:
                expense.setPaidBy(df.columns[i])
                # arrondi inferieur 
                total = math.floor(col / (nbParticipant - 1) * nbParticipant)
                expense.setCoutTotal(total)
            elif nbParticipant == 1 :
                expense.setPaidBy(df.columns[i])
                # arrondi inferieur 
                total = round(col,2)
                expense.setCoutTotal(total)
            i += 1

        resultExpenseListe.append(expense)

    return resultExpenseListe

def getExpensePerParticipant(fileName):
    # Chargement le fichier CSV dans un DataFrame
    df = pd.read_csv(fileName)

    resultParticipantTotal = []

    participantNames = df.columns[2:]

    for name in participantNames:
        nameValues = df[name].to_list()
        total = 0
        for val in nameValues:
            total += float(val)
        total = round(total,2)
        participantTotal = Classes.ParticipantTotal(name, total)
        resultParticipantTotal.append(participantTotal)
    
    return resultParticipantTotal

def isCSVEmpty(fileName):
    # Chargement le fichier CSV dans un DataFrame
    df = pd.read_csv(fileName)

    result = False

    # vérif si le dataframe est vide
    if df.empty:
        result = True

    return result

def getAllParticipant(fileName):
    # Chargement le fichier CSV dans un DataFrame
    df = pd.read_csv(fileName)

    participantNames = df.columns[2:]
    
    return participantNames
    