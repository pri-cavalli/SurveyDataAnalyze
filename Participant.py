import Ocean
import AgilePractice as ag

class Participant:
    def __init__(self, answers):
        self.personalData = []
        self.affirmatives = []
        self.experiences = []

        ipipTest = []
        pilot = []
        copilot = []
        index = 0
        for answer in answers:
            if index >= 0 and index <= 8: 
                self.personalData.insert(len(self.personalData), answer)
            if index >= 9 and index <= 14:
                pilot.insert(len(pilot), answer)
            if index >= 15 and index <= 20:
                copilot.insert(len(copilot), answer)
            if index >= 67 and index <= 116:
                ipipTest.insert(len(ipipTest), answer)
            index+=1
        self.ocean = Ocean.Ocean(ipipTest)
        self.copilot = ag.AgilePractice(ag.PracticeType.copilot, copilot)
        self.pilot = ag.AgilePractice(ag.PracticeType.pilot, pilot)