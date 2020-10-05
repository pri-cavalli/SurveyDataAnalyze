import csv
import math
import pandas as pd
import Participant
import AgilePractice as ag
import matplotlib.pyplot as plt

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
    df2.plot.hist(bins=50)

def plotPilotExpertise():
    participants = getParticipantsFromCsv()
    pilots = []
    for p in participants:
        pilots.insert(0, ag.expertiseValue[p.pilot.expertise])
    data = {
        "Pilot": [
            pilots.count(ag.expertiseValue[1]),
            pilots.count(ag.expertiseValue[2]),
            pilots.count(ag.expertiseValue[3]),
            pilots.count(ag.expertiseValue[4]),
            pilots.count(ag.expertiseValue[5]),
        ],
        "Experience in pair programing": [
            ag.expertiseValue[1],
            ag.expertiseValue[2],
            ag.expertiseValue[3],
            ag.expertiseValue[4],
            ag.expertiseValue[5],
        ]
    }
    df = pd.DataFrame(data)
    df.plot(x='Experience in pair programing', y='Pilot', kind='bar')
    plt.xticks(rotation=45)

def plotPairProgrammingExpertise():
    participants = getParticipantsFromCsv()
    print(participants[0].pilot.expertise)
    print(participants[0].copilot.expertise)
    both = []
    for p in participants:
        both.insert(0, [p.copilot.expertise, p.pilot.expertise])
    df2 = pd.DataFrame(both, columns=['Copilot', 'Pilot'])
    df2.plot.hist(alpha=0.6, bins=5)

    both2 = []
    for p in participants:
        both2.insert(0, [p.pilot.expertise])
        both2.insert(0, [p.copilot.expertise])
    df2 = pd.DataFrame(both2, columns=['Pair programming'])
    df2.plot.hist(bins=5)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html