from enum import Enum

class PracticeType(Enum):
    pilot = "Pair Programming being Pilot",
    copilot = "Pair Programming being Co-pilot",
    reviewer = "Code Review being Reviewer",
    author = "Code Review being Author",
    planning = "Scrum Planning Meeting",
    daily = "Scrum Daily Meeting",
    review = "Scrum Review Meeting",
    retrospective = "Scrum Retrospective Meeting",
    design = "Design Meeting",

PracticeQuestion = {
    "pilot": " da atividade de programação em pares como piloto.",
    "copilot": " da atividade de programação em pares como co-piloto.",
    "reviewer": " da atividade de revisão de código como revisor.",
    "author": " da atividade de revisão de código como autor.",
    "planning": " da reunião Planning",
    "daily": " da reunião Daily",
    "review": " da reunião Review",
    "retrospective": " da reunião Retrospective",
    "design": " de reuniões de discussão de design.",
}
FeelingTranslate = {
    "confort": "Conforto",
    "pleasure": "Prazer",
    "respected": "Respeitado",
    "safe": "Seguro",
    "tiring": "Cansado"
}

FeelingQuestion = {
    "confort": "Sinto confortável ao participar",
    "pleasure": "Tenho prazer em participar",
    "respected": "Sinto respeitado pelos meus colegas ao participar",
    "safe": "Sinto seguro ao participar",
    "tiring": "Considero cansativo participar"
}

expertiseValue = {
    1: "None",
    2: "Small",
    3: "Some",
    4: "High",
    5: "Expert"
}

linkertValue = {
    "Concordo fortemente": 7,
    "Concordo": 6,
    "Concordo fracamente": 5,
    "Neutro": 4,
    "Discordo fracamente": 3,
    "Discordo": 2,
    "Discordo fortemente": 1
}

class AgilePractice:
    def __init__(self, practiceType, answers):
        self.type = practiceType
        self.answers = answers
        self.expertise = answers[0]
        self.confort = linkertValue[answers[1]]
        self.pleasure = linkertValue[answers[2]]
        self.tiring = linkertValue[answers[3]]
        self.respected = linkertValue[answers[4]]
        self.safe = linkertValue[answers[5]]

    def __getitem__(self, key):
        return getattr(self, key)
        
    def __setitem__(self, key, value):
        return setattr(self, key, value)