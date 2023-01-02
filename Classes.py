class CoutParticipant:
    def __init__(self, cout, participant):
        self.cout = cout
        self.participant = participant

    def getCout(self):
        return self.cout

    def getParticipant(self):
        return self.participant

class Expense:
    def __init__(self, libelle, coutTotal, paidBy):
        self.libelle = libelle
        self.coutTotal = coutTotal
        self.paidBy = paidBy

    def getLibelle(self):
        return self.libelle

    def setLibelle(self, libelle):
        self.libelle = libelle

    def getCoutTotal(self):
        return self.coutTotal

    def setCoutTotal(self, coutTotal):
        self.coutTotal = coutTotal

    def getPaidBy(self):
        return self.paidBy

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy
    
    def display(self):
        print('Libelle : ' + self.libelle + '/ Cout Total : ' + str(self.coutTotal) + '/ Payé par : ' + self.paidBy)