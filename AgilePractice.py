agilePracticeType = {
        'pilot': "Pair Programming being Pilot",
        'copilot': "Pair Programming being Co-pilot",
        'reviewer': "Code Review being Reviewer",
        'author': "Code Review being Author",
        'planning': "Scrum Planning Meeting",
        'daily': "Scrum Daily Meeting",
        'review': "Scrum Review Meeting",
        'retrospective': "Scrum Retrospective Meeting",
        'design': "Design Meeting",
    }

expertiseValue = {
        1: "None experience",
        2: "Small experience",
        3: "Some experience",
        4: "High experience",
        5: "Expert"
    }

class AgilePractice:
    def __init__(self, practiceType, answers):
        self.type = AgilePractice
        self.answers = answers
        self.expertise = answers[0]
        self.confort = answers[1]
        self.pleasure = answers[2]
        self.tiring = answers[3]
        self.respected = answers[4]
        self.safe = answers[5]