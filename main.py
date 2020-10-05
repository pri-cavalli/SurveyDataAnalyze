import csv
import math
import pandas as pd
import Participant

def createParticipants(surveyData):
    participants = []
    participantIndex = 0
    for participantAnswers in surveyData:
        participant = Participant.Participant(participantAnswers)
        participants.insert(0,participant)
        participantIndex+=1
    return participants

def getParticipantsFromCsv():
    survey = pd.read_csv('data.csv')
    surveyData = survey.values
    return createParticipants(surveyData)

def plotBoxOcean():
    participants = getParticipantsFromCsv()
    oceanPerParticipant = []
    for p in participants:
        oceanPerParticipant.insert(0, [
            p.ocean.openess,
            p.ocean.conscientiousness,
            p.ocean.extroversion,
            p.ocean.agreeableness,
            p.ocean.neuroticism
        ])

    df2 = pd.DataFrame(oceanPerParticipant, columns=['O', 'C', 'E', 'A', 'N'])
    df2.plot.box()

def plotHistExtroversion():
    participants = getParticipantsFromCsv()
    extrovesions = []
    for p in participants:
        extrovesions.insert(0, [p.ocean.extroversion])

    df2 = pd.DataFrame(extrovesions, columns=['Extroversion'])
    df2.plot.hist()
