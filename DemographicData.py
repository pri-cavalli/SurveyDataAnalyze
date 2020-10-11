def printData(participants):
    ageData(participants)
    print("-")
    genderData(participants)
    print("-")
    bornCountryData(participants)
    print("-")
    studyData(participants)
    print("-")
    courseData(participants)
    print("-")
    experienceData(participants)
    print("-")
    expertiseData(participants)


def ageData(participants):
    less20years = 0
    between20and30years = 0
    between30and40years = 0
    more40years = 0
    total = len(participants)
    for p in participants:
        if int(p.personalData[1]) < 20:
            less20years += 1
        elif int(p.personalData[1]) < 30:
            between20and30years += 1
        elif int(p.personalData[1]) < 40:
            between30and40years += 1
        else:
            more40years += 1
    print("Age < 20 {v:.0f}# {p:.2f}%".format(v=less20years, p=less20years * 100 / total) )
    print("Age 20-29 {v:.0f}# {p:.2f}%".format(v=between20and30years, p=between20and30years * 100 / total) )
    print("Age 30-39 {v:.0f}# {p:.2f}%".format(v=between30and40years, p=between30and40years * 100 / total) )
    print("Age > 40 {v:.0f}# {p:.2f}%".format(v=more40years, p=more40years * 100 / total) )

def genderData(participants):
    male = 0
    female = 0
    noBi = 0
    other = 0
    total = len(participants)
    for p in participants:
        if p.personalData[2] == "Masculino":
            male += 1
        elif p.personalData[2] == "Feminino":
            female += 1
        elif p.personalData[2] == "Não Binário":
            noBi += 1
        else:
            other += 1
    print("Male {v:.0f}# {p:.2f}%".format(v=male, p=male * 100 / total) )
    print("Female {v:.0f}# {p:.2f}%".format(v=female, p=female * 100 / total) )
    print("Não Binário {v:.0f}# {p:.2f}%".format(v=noBi, p=noBi * 100 / total) )
    print("Prefiro não informar {v:.0f}# {p:.2f}%".format(v=other, p=other * 100 / total) )

def bornCountryData(participants):
    br = 0
    outro = 0
    total = len(participants)
    for p in participants:
        if p.personalData[3] == "Brasileiro":
            br += 1
        else:
            outro += 1
    print("br {v:.0f}# {p:.2f}%".format(v=br, p=br * 100 / total) )
    print("outro {v:.0f}# {p:.2f}%".format(v=outro, p=outro * 100 / total) )

def livingCountryData(participants):
    br = 0
    outro = 0
    total = len(participants)
    for p in participants:
        if p.personalData[4] == "Brasil":
            br += 1
        else:
            outro += 1
    print("reside no br {v:.0f}# {p:.2f}%".format(v=br, p=br * 100 / total) )
    print("outro {v:.0f}# {p:.2f}%".format(v=outro, p=outro * 100 / total) )

def studyData(participants):
    bachareladoI = 0
    bachareladoC = 0
    mestradoI = 0
    mestradoC = 0
    doutoradoI = 0
    doutoradoC = 0
    other = 0
    total = len(participants)
    for p in participants:
        if p.personalData[5] == "Bacharelado incompleto":
            bachareladoI += 1
        elif p.personalData[5] == "Bacharelado completo":
            bachareladoC += 1
        elif p.personalData[5] == "Mestrado incompleto":
            mestradoI += 1
        elif p.personalData[5] == "Mestrado completo":
            mestradoC += 1
        elif p.personalData[5] == "Doutorado incompleto":
            doutoradoI += 1
        elif p.personalData[5] == "Doutorado completo":
            doutoradoC += 1
        else:
            other += 1
    print("bachareladoI {v:.0f}# {p:.2f}%".format(v=bachareladoI, p=bachareladoI * 100 / total) )
    print("bachareladoC {v:.0f}# {p:.2f}%".format(v=bachareladoC, p=bachareladoC * 100 / total) )
    print("mestradoI {v:.0f}# {p:.2f}%".format(v=mestradoI, p=mestradoI * 100 / total) )
    print("mestradoC {v:.0f}# {p:.2f}%".format(v=mestradoC, p=mestradoC * 100 / total) )
    print("doutoradoI {v:.0f}# {p:.2f}%".format(v=doutoradoI, p=doutoradoI * 100 / total) )
    print("doutoradoC {v:.0f}# {p:.2f}%".format(v=doutoradoC, p=doutoradoC * 100 / total) )
    print("Outro {v:.0f}# {p:.2f}%".format(v=other, p=other * 100 / total) )
    

def courseData(participants):
    cic = 0
    ecp = 0
    si = 0
    es = 0
    ads = 0
    jd = 0
    other = 0
    total = len(participants)
    for p in participants:
        if p.personalData[6] == "Ciência da computação":
            cic += 1
        elif p.personalData[6] == "Engenharia da computação":
            ecp += 1
        elif p.personalData[6] == "Sistemas de informação":
            si += 1
        elif p.personalData[6] == "Engenharia de software":
            es += 1
        elif p.personalData[6] == "Análise e Desenvolvimento de Sistemas":
            ads += 1
        elif p.personalData[6] == "Jogos Digitais":
            jd += 1
        else:
            other += 1
    print("cic {v:.0f}# {p:.2f}%".format(v=cic, p=cic * 100 / total) )
    print("ecp {v:.0f}# {p:.2f}%".format(v=ecp, p=ecp * 100 / total) )
    print("si {v:.0f}# {p:.2f}%".format(v=si, p=si * 100 / total) )
    print("es {v:.0f}# {p:.2f}%".format(v=es, p=es * 100 / total) )
    print("ads {v:.0f}# {p:.2f}%".format(v=ads, p=ads * 100 / total) )
    print("jd {v:.0f}# {p:.2f}%".format(v=jd, p=jd * 100 / total) )
    print("Outro {v:.0f}# {p:.2f}%".format(v=other, p=other * 100 / total) )

def experienceData(participants):
    two = 0
    twoFive = 0
    fiveTen = 0
    ten = 0
    total = len(participants)
    for p in participants:
        if p.personalData[7] == "Menos de 2 anos":
            two += 1
        elif p.personalData[7] == "Entre 2 a 5 anos":
            twoFive += 1
        elif p.personalData[7] == "Entre 5 e 10 anos":
            fiveTen += 1
        elif p.personalData[7] == "Mais de 10 anos":
            ten += 1
    print("2 years {v:.0f}# {p:.2f}%".format(v=two, p=two * 100 / total) )
    print("2-5 {v:.0f}# {p:.2f}%".format(v=twoFive, p=twoFive * 100 / total) )
    print("5-10 {v:.0f}# {p:.2f}%".format(v=fiveTen, p=fiveTen * 100 / total) )
    print("> 10 {v:.0f}# {p:.2f}%".format(v=ten, p=ten * 100 / total) )

def expertiseData(participants):
    veryLow = 0
    low = 0
    medium = 0
    high = 0
    veryHigh = 0
    total = len(participants)
    for p in participants:
        if p.personalData[8] == "Muito baixo":
            veryLow += 1
        elif p.personalData[8] == "Baixo":
            low += 1
        elif p.personalData[8] == "Médio":
            medium += 1
        elif p.personalData[8] == "Alto":
            high += 1
        elif p.personalData[8] == "Muito alto":
            veryHigh += 1
    print("veryLow {v:.0f}# {p:.2f}%".format(v=veryLow, p=veryLow * 100 / total) )
    print("low {v:.0f}# {p:.2f}%".format(v=low, p=low * 100 / total) )
    print("medium {v:.0f}# {p:.2f}%".format(v=medium, p=medium * 100 / total) )
    print("high {v:.0f}# {p:.2f}%".format(v=high, p=high * 100 / total) )
    print("veryHigh {v:.0f}# {p:.2f}%".format(v=veryHigh, p=veryHigh * 100 / total) )

