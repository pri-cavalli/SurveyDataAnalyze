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

def plotScatterForAffirmativeAndAllPractices(affirmative):
    plotScatterForAffirmativeAndPractice("pilot", affirmative)
    plotScatterForAffirmativeAndPractice("copilot", affirmative)
    plotScatterForAffirmativeAndPractice("author", affirmative)
    plotScatterForAffirmativeAndPractice("reviewer", affirmative)
    plotScatterForAffirmativeAndPractice("planning", affirmative)
    plotScatterForAffirmativeAndPractice("daily", affirmative)
    plotScatterForAffirmativeAndPractice("retrospective", affirmative)
    plotScatterForAffirmativeAndPractice("review", affirmative)
    plotScatterForAffirmativeAndPractice("design", affirmative)

def plotScatterForAffirmativeAndPractice(practiceName, affirmative):
    participants = getParticipantsFromCsv()
    extro = []
    intro = []
    rest = []
    for p in participants:
        if p[practiceName].expertise > 1:
            if p.extroversionLevel == Participant.ExtroversionLevel.extro:
                extro.insert(1, [p.ocean.extroversion, p[practiceName][affirmative]])
            elif p.extroversionLevel == Participant.ExtroversionLevel.intro:
                intro.insert(1, [p.ocean.extroversion, p[practiceName][affirmative]])
            else: 
                rest.insert(1, [p.ocean.extroversion, p[practiceName][affirmative]])
    df = pd.DataFrame(extro, columns=['Extroversão', practiceName])
    ax = df.plot.scatter(y=practiceName, x="Extroversão", color='Blue', alpha=0.5, label="extro")

    df2 = pd.DataFrame(intro, columns=['Extroversão', practiceName])
    ax2 = df2.plot.scatter(y=practiceName, x="Extroversão", color='Green', alpha=0.2, ax=ax, label="intro")

    df3 = pd.DataFrame(rest, columns=['Extroversão', practiceName])
    df3.plot.scatter(y=practiceName, x="Extroversão", color='Black', alpha=0.5, ax=ax2, label="rest")

def plotBarAffirmatives(affirmative):
    plotBarAffirmative("pilot", affirmative)
    plotBarAffirmative("copilot", affirmative)
    plotBarAffirmative("author", affirmative)
    plotBarAffirmative("reviewer", affirmative)
    plotBarAffirmative("planning", affirmative)
    plotBarAffirmative("daily", affirmative)
    plotBarAffirmative("retrospective", affirmative)
    plotBarAffirmative("review", affirmative)
    plotBarAffirmative("design", affirmative)

def plotBarAffirmative(practiceName, affirmative):
    participants = getParticipantsFromCsv()
    extro = []
    intro = []
    intro2 = []
    for p in participants:
        if p[practiceName].expertise > 1:
            if p.extroversionLevel == Participant.ExtroversionLevel.extro:
                extro.insert(0, p[practiceName][affirmative])
            elif p.extroversionLevel == Participant.ExtroversionLevel.intro:
                intro.insert(0, p[practiceName][affirmative])
    introData = {
        practiceName: [
            intro.count(1),
            intro.count(2),
            intro.count(3),
            intro.count(4),
            intro.count(5),
            intro.count(6),
            intro.count(7),
        ],
        "Linkert": [ 1, 2, 3, 4, 5, 6, 7 ]
    }
    df = pd.DataFrame(introData)
    df.plot(x="Linkert", y=practiceName, kind='bar', color='Green')
    extroData = {
        practiceName: [
            extro.count(1),
            extro.count(2),
            extro.count(3),
            extro.count(4),
            extro.count(5),
            extro.count(6),
            extro.count(7),
        ],
        "Linkert": [ 1, 2, 3, 4, 5, 6, 7 ]
    }
    df2 = pd.DataFrame(extroData)
    df2.plot(x="Linkert", y=practiceName, kind='bar', color='Blue')

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html