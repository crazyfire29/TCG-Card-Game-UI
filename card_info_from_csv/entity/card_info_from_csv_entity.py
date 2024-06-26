
class CardInfoFromCsv:
    __cardNumber = None
    __cardName = None
    __cardRace = None
    __cardGrade = None
    __cardType = None
    __cardJob = None
    __cardEnergy = None
    __cardAttack = None
    __cardPassive = None
    __cardSkill = None
    __cardHp = None
    __cardSKillCounter = None
    __cardSkillFirst = None
    __cardSkillSecond = None
    __cardPassiveFirst = None
    __cardPassiveSecond = None
    __cardSkillFirstDamage = None
    __cardSkillSecondDamage = None
    __cardPassiveFirstDamage = None
    __cardPassiveSecondDamage = None
    __cardSkillFirstUndeadEnergyRequired = None
    __cardSkillFirstHumanEnergyRequired = None
    __cardSkillFirstTrentEnergyRequired = None
    __cardSkillSecondUndeadEnergyRequired = None
    __cardSkillSecondHumanEnergyRequired = None
    __cardSkillSecondTrentEnergyRequired = None

    def __init__(self, record):
        self.__cardNumber = record[0]
        self.__cardName = record[1]
        self.__cardRace = record[2]
        self.__cardGrade = record[3]
        self.__cardType = record[4]
        self.__cardJob = record[5]
        self.__cardEnergy = record[6]
        self.__cardAttack = record[7]
        self.__cardPassive = record[8]
        self.__cardSkill = record[9]
        self.__cardHp = record[10]
        self.__cardSKillCounter = record[11]
        self.__cardSkillFirst = record[12]
        self.__cardSkillSecond = record[13]
        self.__cardPassiveFirst = record[14]
        self.__cardPassiveSecond = record[15]
        self.__cardSkillFirstDamage = record[16]
        self.__cardSkillSecondDamage = record[17]
        self.__cardPassiveFirstDamage = record[18]
        self.__cardPassiveSecondDamage = record[19]
        self.__cardSkillFirstUndeadEnergyRequired = record[20]
        self.__cardSkillFirstHumanEnergyRequired = record[21]
        self.__cardSkillFirstTrentEnergyRequired = record[22]
        self.__cardSkillSecondUndeadEnergyRequired = record[23]
        self.__cardSkillSecondHumanEnergyRequired = record[24]
        self.__cardSkillSecondTrentEnergyRequired = record[25]

    def getCardNumber(self):
        return self.__cardNumber
    def getCardName(self):
        return self.__cardName

    def getCardRace(self):
        return self.__cardRace

    def getCardGrade(self):
        return self.__cardGrade

    def getCardType(self):
        return self.__cardType

    def getCardJob(self):
        return self.__cardJob

    def getCardEnergy(self):
        return self.__cardEnergy

    def getCardAttack(self):
        return self.__cardAttack

    def getCardPassive(self):
        return self.__cardPassive

    def getCardSkill(self):
        return self.__cardSkill

    def getCardHp(self):
        return self.__cardHp
    def getCardSkillCounter(self):
        return self.__cardSKillCounter

    def getCardSkillFirst(self):
        return self.__cardSkillFirst

    def getCardSkillSecond(self):
        return self.__cardSkillSecond

    def getCardPassiveFirst(self):
        return self.__cardPassiveFirst

    def getCardPassiveSecond(self):
        return self.__cardPassiveSecond

    def getCardSkillFirstDamage(self):
        return self.__cardSkillFirstDamage

    def getCardSkillSecondDamage(self):
        return self.__cardSkillSecondDamage

    def getCardPassiveFirstDamage(self):
        return self.__cardPassiveFirstDamage

    def getCardPassiveSecondDamage(self):
        return self.__cardPassiveSecondDamage

    def getCardSkillFirstUndeadEnergyRequired(self):
        return self.__cardSkillFirstUndeadEnergyRequired

    def getCardSkillFirstHumanEnergyRequired(self):
        return self.__cardSkillFirstHumanEnergyRequired

    def getCardSkillFirstTrentEnergyRequired(self):
        return self.__cardSkillFirstTrentEnergyRequired

    def getCardSkillSecondUndeadEnergyRequired(self):
        return self.__cardSkillSecondUndeadEnergyRequired

    def getCardSkillSecondHumanEnergyRequired(self):
        return self.__cardSkillSecondHumanEnergyRequired

    def getCardSkillSecondTrentEnergyRequired(self):
        return self.__cardSkillSecondTrentEnergyRequired
