import globales
import pandas as pd

def createCSV(fileName, participants):

    header = ['LibelleDepense']
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
    
    # Ajout du libelle 
    newDf = pd.DataFrame(dtype=object)
    newDf.loc[currentIndex, 'LibelleDepense'] = expenseName

    for coutParticipant in listCoutParticipant:
        if coutParticipant.getParticipant() == paidBy:
            # Remplir les valeurs de la nouvelle ligne
            newDf.loc[currentIndex, coutParticipant.getParticipant()] = + float(coutParticipant.getCout())
        else:
            # Remplir les valeurs de la nouvelle ligne
            newDf.loc[currentIndex, coutParticipant.getParticipant()] = - float(coutParticipant.getCout())
        
    newDf.to_csv(fileName, mode='a', index=None, header=False)