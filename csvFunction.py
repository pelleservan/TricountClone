import globales
import pandas as pd

def createCSV(fileName, participants):

    header = ['LibelleDepense']
    header.extend(participants)
    df = pd.DataFrame(columns=header)

    df.to_csv(fileName + '.csv', index=None, header=True)