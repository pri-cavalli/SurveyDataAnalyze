import csv

ascIpipAnswer = {
    'Muito preciso': 5,
    'Moderadamente preciso': 4,
    'Nem impreciso nem preciso': 3,
    'Moderadamente impreciso': 2,
    'Muito impreciso': 1,
}

descIpipAnswer = {
    'Muito preciso': 1,
    'Moderadamente preciso': 2,
    'Nem impreciso nem preciso': 3,
    'Moderadamente impreciso': 4,
    'Muito impreciso': 5,
}

def mapIpipItemAndExtroversionScore(index, answer):
    item = index + 1
    if item == 1 or item == 11 or item == 21 or item == 31 or item == 41:
        return ascIpipAnswer[answer]
    if item == 6 or item == 16 or item == 26 or item == 36 or item == 46:
        return descIpipAnswer[answer]
    return 0

def mapIpipTestAndExtroversionScore(answers):
    acc = 0
    index = 0
    for answer in answers:
        acc += mapIpipItemAndExtroversionScore(index, answer)
        index += 1
    return acc

class Participant:

    def __init__(self, answers):
        self.personalData = []
        self.affirmatives = []
        self.experiences = []
        self.ipipTest = []
        self.extroversion = 0

        index = 0
        for answer in answers:
            if index >= 0 and index <= 8: 
                self.personalData.insert(len(self.personalData), answer)
            if index >= 67 and index <= 116:
                self.ipipTest.insert(len(self.ipipTest), answer)
            index+=1
        self.calculateOCEAN()

    def calculateOCEAN(self):
        self.extroversion = mapIpipTestAndExtroversionScore(self.ipipTest)


def createParticipants(surveyData):
    participants = []
    participantIndex = 0
    for participantAnswers in surveyData:
        if participantIndex != 0:
            participant = Participant(participantAnswers)
            participants.insert(0,participant)
        participantIndex+=1
    return participants

with open('data.csv') as csv_file:
    surveyData = csv.reader(csv_file, delimiter=',')

    participants = createParticipants(surveyData)
    # for p in participants:
    #     print(p.extroversion)

