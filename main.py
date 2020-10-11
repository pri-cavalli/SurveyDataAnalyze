import csv
import math
import pandas as pd
import Participant
import AgilePractice as ag
import matplotlib.pyplot as plt
from scipy import stats
import statistics
import DemographicData

def createParticipants(surveyData):
    participants = []
    participantIndex = 0
    for participantAnswers in surveyData:
        participant = Participant.Participant(participantAnswers)
        participants.insert(0,participant)
        participantIndex+=1
    extroversions = list(map(lambda p: p.ocean.extroversion, participants))
    qt = stats.mstats.mquantiles(extroversions, prob=[0.2, 0.4, 0.6, 0.8],alphap=0.5, betap=0.5)

    for p in participants:
        p.rankExtroversionLevel(qt)

    return participants

def getParticipantsFromCsv():
    survey = pd.read_csv('data.csv')
    surveyData = survey.values
    return createParticipants(surveyData)

def age():
    participants = getParticipantsFromCsv()

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
    points = []
    for p in participants:
        extrovesions.insert(0, [p.ocean.extroversion])
        points.insert(0, p.ocean.extroversion)
    print(max(points))
    print(min(points))
    print(statistics.median(points))
    df2 = pd.DataFrame(extrovesions, columns=['Extroversão'])
    df2.plot.hist(bins=41,range=[10, 50])

def plotPieGrossExtroversion():
    participants = getParticipantsFromCsv()
    extro = 0
    intro = 0
    neutral = 0
    total = len(participants)
    for p in participants:
        extroversion = p.ocean.extroversion
        if (extroversion >= 40 ):
            extro+=1
        elif (extroversion <= 20 ):
            intro+=1
        else:
            neutral+=1

    series = pd.Series(
        [intro, neutral, extro],
        index=['Introvertidos', 'Neutros', 'Extrovertidos'],
        name="")
    series.plot.pie(
        figsize=(6, 6),
        colors=['b', 'c', 'g'],
        autopct=lambda perc: '{p:.2f}%  ({v:.0f})'.format(p=perc,v=perc * total / 100)
    )

def plotPiePatternExtroversion():
    participants = getParticipantsFromCsv()
    extroversions = list(map(lambda p: p.ocean.extroversion, participants))
    shapiro_test = stats.shapiro(extroversions)
    print(shapiro_test)
    extro = 0
    somewhatExtro = 0
    average = 0
    somewhatIntro = 0
    intro = 0
    total = len(participants)
    for participant in participants:
        if (participant.extroversionLevel == Participant.ExtroversionLevel.intro ):
            intro+=1
        elif (participant.extroversionLevel == Participant.ExtroversionLevel.littleIntro ):
            somewhatIntro+=1
        elif (participant.extroversionLevel == Participant.ExtroversionLevel.neutral ):
            average+=1
        elif (participant.extroversionLevel == Participant.ExtroversionLevel.littleExtro ):
            somewhatExtro+=1
        else:
            extro+=1

    series = pd.Series(
        [intro, somewhatIntro, average, somewhatExtro, extro],
        index=['Introvertidos', 'Pouco Introvertidos', 'Neutros','Pouco Extrovertidos', 'Extrovertidos'],
        name="")
    series.plot.pie(
        figsize=(6, 6),
        autopct=lambda perc: '{p:.2f}%  ({v:.0f})'.format(p=perc,v=perc * total / 100)
    )

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
    both = []
    for p in participants:
        both.insert(0, [p.copilot.expertise, p.pilot.expertise])
    df2 = pd.DataFrame(both, columns=['Copilot', 'Pilot'])
    df2.plot.hist(alpha=0.6, bins=5)

def plotCodeReviewExpertise():
    participants = getParticipantsFromCsv()
    both = []
    for p in participants:
        both.insert(0, [p.reviewer.expertise, p.author.expertise])
    df2 = pd.DataFrame(both, columns=['Reviewer', 'Author'])
    df2.plot.hist(alpha=0.6, bins=5)

def demographicData():
    participants = getParticipantsFromCsv()
    intro = list(filter(lambda p: p.extroversionLevel == Participant.ExtroversionLevel.intro, participants))
    extro = list(filter(lambda p: p.extroversionLevel == Participant.ExtroversionLevel.extro, participants))
    print("-----All:")
    DemographicData.printData(participants)
    print("-----Intro:")
    DemographicData.printData(intro)
    print("-----Extro:")
    DemographicData.printData(extro)

def plotScatterPairProgramming(affirmative):
    plotScatterPractice("pilot", affirmative)
    plotScatterPractice("copilot", affirmative)

def plotScatterPractice(practiceName, affirmative):
    participants = getParticipantsFromCsv()
    practice = []
    for p in participants:
        if p[practiceName].expertise > 1:
            practice.insert(1, [p.ocean.extroversion, p[practiceName][affirmative]])
    practice.sort(key=lambda e:ag.linkertValue[e[1]])
    df = pd.DataFrame(practice, columns=['Extroversão', practiceName])
    df.plot.scatter(y=practiceName, x="Extroversão", color='DarkBlue', label='All', alpha=0.4)


# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html