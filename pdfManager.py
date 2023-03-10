from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table
import pandas as pd

import tkinter as tk
import os
import configFunction

def editPDF(currentAccount, username):
    popup = tk.Tk()
    popup.title("Warning")
    label = tk.Label(popup, text="your pdf file is available in : "+str(os.getcwd()))
    label.pack()

    doc = SimpleDocTemplate("./"+str(currentAccount.replace(" ", "_"))+".pdf", pagesize=letter)

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    title = getSampleStyleSheet()
    title['Normal'].textColor = '#FFA500'
    title['Normal'].fontSize = 25
    title['Normal'].leading = 30

    subTitle = getSampleStyleSheet()
    subTitle['Normal'].fontSize = 18
    subTitle['Normal'].leading = 25

    styleRed = getSampleStyleSheet()
    styleRed['Normal'].backColor = "#ff7866"

    styleGreen = getSampleStyleSheet()
    styleGreen['Normal'].backColor = "#b3ff9c"

    content = []

    content.append(Paragraph("Account : "+str(currentAccount), title['Normal']))

    content.append(Paragraph("Created by "+str(username), subTitle['Normal']))

    currentAccountExpensesFile = configFunction.getCSVFilePath(currentAccount)
    expenses = pd.read_csv(currentAccountExpensesFile)

    content.append(Paragraph("Participants : "+str(', '.join(expenses.columns[2:].to_list())), style))

    content.append(Paragraph("Expenses :", subTitle['Normal']))
    expenses = expenses.drop('nbParticipants', axis=1)
    expenses[expenses.columns[3:]] = expenses[expenses.columns[3:]].astype(float)
    expenses = expenses.rename(columns={'LibelleDepense': 'title'})
    expenses['Total'] = expenses[expenses.columns[1:-1]].max(axis=1)

    total = {'title' : 'Total'}

    for col in expenses.columns[1:]:
        total[col] = round(expenses[col].sum(), 2)

    expenses = expenses.append(total, ignore_index=True)

    expensesTable = [expenses.columns.tolist()] + expenses.values.tolist()

    expensesTable = Table(expensesTable)

    expensesTable.setStyle([('BACKGROUND', (0, 0), (-1, 0), '#FFA500'),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BACKGROUND', (0, -1), (-1, -1), '#323232'),
                    ('TEXTCOLOR', (0, -1), (-1, -1), colors.whitesmoke),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    content.append(expensesTable)

    content.append(Paragraph("Balance :", subTitle['Normal']))

    for participant in expenses.columns[1:-1]:
        value = expenses.loc[expenses.index[-1], participant]
        if value > 0:
            content.append(Paragraph(str(participant)+" : "+str(value), styleGreen['Normal']))
        elif value < 0:
            content.append(Paragraph(str(participant)+" : "+str(value), styleRed['Normal']))
        else:content.append(str(participant)+" : "+str(value), style)

    doc.build(content)

    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack()
    popup.mainloop()
