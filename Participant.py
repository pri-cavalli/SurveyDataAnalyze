import Ocean
import AgilePractice as ag
from enum import Enum

class ExtroversionLevel(Enum):
    intro = "Introvertido",
    littleIntro = "Pouco Introvertido",
    neutral = "Neutro",
    littleExtro = "Pouco Extrovertido",
    extro = "Extrovertido"

class Participant:
    def __init__(self, answers):
        self.personalData = []
        self.affirmatives = []
        self.experiences = []

        ipipTest = []
        pilot = []
        copilot = []
        reviewer = []
        author = []
        index = 0
        for answer in answers:
            if index >= 0 and index <= 8: 
                self.personalData.insert(len(self.personalData), answer)
            if index >= 9 and index <= 14:
                pilot.insert(len(pilot), answer)
            if index >= 15 and index <= 20:
                copilot.insert(len(copilot), answer)
            if index >= 22 and index <= 27:
                reviewer.insert(len(reviewer), answer)
            if index >= 28 and index <= 33:
                author.insert(len(author), answer)
            if index >= 67 and index <= 116:
                ipipTest.insert(len(ipipTest), answer)
            index+=1
        self.ocean = Ocean.Ocean(ipipTest)
        self.copilot = ag.AgilePractice(ag.PracticeType.copilot, copilot)
        self.pilot = ag.AgilePractice(ag.PracticeType.pilot, pilot)
        self.reviewer = ag.AgilePractice(ag.PracticeType.reviewer, reviewer)
        self.author = ag.AgilePractice(ag.PracticeType.author, author)

    def __getitem__(self, key):
        return getattr(self, key)
        
    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def rankExtroversionLevel(self, qt):
        if (self.ocean.extroversion < qt[0] ):
            self.extroversionLevel = ExtroversionLevel.intro
        elif (self.ocean.extroversion < qt[1] ):
            self.extroversionLevel = ExtroversionLevel.littleIntro
        elif (self.ocean.extroversion < qt[2] ):
            self.extroversionLevel = ExtroversionLevel.neutral
        elif (self.ocean.extroversion < qt[3] ):
            self.extroversionLevel = ExtroversionLevel.littleExtro
        else:
            self.extroversionLevel = ExtroversionLevel.extro