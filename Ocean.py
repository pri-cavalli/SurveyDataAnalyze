class Ocean:
    ascScoreAnswer = {
        'Muito preciso': 5,
        'Moderadamente preciso': 4,
        'Nem impreciso nem preciso': 3,
        'Moderadamente impreciso': 2,
        'Muito impreciso': 1,
    }

    descScoreAnswer = {
        'Muito preciso': 1,
        'Moderadamente preciso': 2,
        'Nem impreciso nem preciso': 3,
        'Moderadamente impreciso': 4,
        'Muito impreciso': 5,
    }


    def __init__(self, answers):
        self.ipipTest = answers
        self.openess = 0
        self.conscientiousness = 0
        self.extroversion = 0
        self.agreeableness = 0
        self.neuroticism = 0
        self.calculateOceanScores()

    def __getitem__(self, key):
        return getattr(self, key)
        
    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return "O: %s, C: %s, E: %s, A: %s, N: %s" % (self.openess, self.conscientiousness, self.extroversion, self.agreeableness, self.neuroticism)

    def calculateOceanScores(self):
        index = 0
        for answer in self.ipipTest:
            trait = self.getTraitFromTestItem(index)
            score = self.getScoreFromAnswer(index, answer)
            self[trait] += score
            index += 1

    def getTraitFromTestItem(self, testItem):
        mapItemAndTrait = {
            0: "extroversion",
            1: "agreeableness",
            2: "conscientiousness",
            3: "neuroticism",
            4: "openess"
        }
        return mapItemAndTrait.get(testItem % 5)

    def getScoreFromAnswer(self, index, answer):
        testItem = index + 1
        if testItem == 29 or testItem == 39 or testItem == 49:
            return self.descScoreAnswer[answer]
        if testItem == 40 or testItem == 42 or testItem == 48 or testItem == 50 or testItem % 2 == 1:
            return self.ascScoreAnswer[answer]
        return self.descScoreAnswer[answer]