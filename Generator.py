import random

#This shit would reroll very time user would click generate randomly.

# ___READING FROM FILES!!!___

fileCharName = open('CharacterGenVariations/Base/first-names.txt', "r")
readFileCharName = fileCharName.readlines()
modifiedFileCharName = []
for line in readFileCharName:
    modifiedFileCharName.append(line.strip())

fileCharGen = open('CharacterGenVariations/Base/Gender.txt', "r")
readFileCharGen = fileCharGen.readlines()
modifiedFileCharGen = []
for line in readFileCharGen:
    modifiedFileCharGen.append(line.strip())

fileCharRace = open('CharacterGenVariations/Base/Races.txt', "r")
readFileCharRace = fileCharRace.readlines()
modifiedFileCharRace= []
for line in readFileCharRace:
    modifiedFileCharRace.append(line.strip())


fileCharHairCol = open('CharacterGenVariations/Appearence/hair/Color.txt', "r")
fileCharHairCondAndApp = open('CharacterGenVariations/Appearence/hair/ConditionAndApperance.txt', "r")
fileCharHairPattern = open('CharacterGenVariations/Appearence/hair/Pattern.txt', "r")
fileCharHairTexture = open('CharacterGenVariations/Appearence/hair/Texture.txt', "r")
readFileCharHairCol = fileCharHairCol.readlines()
modifiedFileCharHairCol = []
for line in readFileCharHairCol:
    modifiedFileCharHairCol.append(line.strip())

readFileCharHairCondAndApp = fileCharHairCondAndApp.readlines()
modifiedFileCharHairCondAndApp = []
for line in readFileCharHairCondAndApp:
    modifiedFileCharHairCondAndApp.append(line.strip())

readFileCharHairPattern = fileCharHairPattern.readlines()
modifiedFileCharHairPattern = []
for line in readFileCharHairPattern:
    modifiedFileCharHairPattern.append(line.strip())

readFileCharHairTexture = fileCharHairTexture.readlines()
modifiedFileCharHairTexture = []
for line in readFileCharHairTexture:
    modifiedFileCharHairTexture.append(line.strip())

fileCharEyeColor = open('CharacterGenVariations/Appearence/EyeColor.txt', "r")
readFileCharEyeColor = fileCharEyeColor.readlines()
modifiedFileCharEyeColor = []
for line in readFileCharEyeColor:
    modifiedFileCharEyeColor.append(line.strip())

fileCharBodyDes = open('CharacterGenVariations/Appearence/BodyDes.txt', "r")
readFileCharBodyDes = fileCharBodyDes.readlines()
modifiedFileCharBodyDes = []
for line in readFileCharBodyDes:
    modifiedFileCharBodyDes.append(line.strip())

    
fileCharPersonalityTraitsPos = open('CharacterGenVariations/Personality/Positive/Traits.txt', "r")
fileCharPersonalityTraitsNeut = open('CharacterGenVariations/Personality/Neutral/Traits.txt', "r")
fileCharPersonalityTraitsNeg = open('CharacterGenVariations/Personality/Negative/Traits.txt', "r")

readFileCharPersonalityTraitsPos = fileCharPersonalityTraitsPos.readlines()
modifiedFileCharPersonalityTraitsPos = []
for line in readFileCharPersonalityTraitsPos:
    modifiedFileCharPersonalityTraitsPos.append(line.strip())

readFileCharPersonalityTraitsNeut = fileCharPersonalityTraitsNeut.readlines()
modifiedFileCharPersonalityTraitsNeut = []
for line in readFileCharPersonalityTraitsNeut:
    modifiedFileCharPersonalityTraitsNeut.append(line.strip())

readFileCharPersonalityTraitsNeg = fileCharPersonalityTraitsNeg.readlines()
modifiedFileCharPersonalityTraitsNeg = []
for line in readFileCharPersonalityTraitsNeg:
    modifiedFileCharPersonalityTraitsNeg.append(line.strip())

fileCharBackStories = open('CharacterGenVariations/Personality/BackStories.txt', "r")
readFileCharBackStories = fileCharBackStories.readlines()
modifiedFileCharBackStories = []
for line in readFileCharBackStories:
    modifiedFileCharBackStories.append(line.strip())

"""
# ___CHARACTER GEN___
def charGenerator():
    #base stuff
    characterName = random.choice(modifiedFileCharName)
    characterGender = random.choice(modifiedFileCharGen)
    characterAge = random.randrange(16, 78) #maybe a customisebale range later
    characterRace = random.choice(modifiedFileCharRace) 

    # appearence stuff
    characterHairDescription = (
        random.choice(modifiedFileCharHairCol),
        random.choice(modifiedFileCharHairCondAndApp),
        random.choice(modifiedFileCharHairPattern),
        random.choice(modifiedFileCharHairTexture),)
    characterEyeColor = random.choice(modifiedFileCharEyeColor)
    heightInCm = random.randrange(155, 214)
    heightInFeet = heightInCm / 30.48
    characterHeight = (f"Cm: {heightInCm} / Feet: {heightInFeet:.2f}") #feet or cm option
    characterBodyDecription = random.choice(modifiedFileCharBodyDes); 

    # personality stuff
    characterPersonalityTraits= (
        random.choice(modifiedFileCharPersonalityTraitsPos),
        random.choice(modifiedFileCharPersonalityTraitsPos),
        random.choice(modifiedFileCharPersonalityTraitsPos),
        random.choice(modifiedFileCharPersonalityTraitsNeut),
        random.choice(modifiedFileCharPersonalityTraitsNeut),
        random.choice(modifiedFileCharPersonalityTraitsNeg),
        random.choice(modifiedFileCharPersonalityTraitsNeg),
        random.choice(modifiedFileCharPersonalityTraitsNeg)
    ) #three pos, two neut, three neg
    characterBackstory = random.choice(modifiedFileCharBackStories)
    readyCharacter = characterName, characterGender, characterAge, characterEyeColor, characterHairDescription, characterHeight, characterBodyDecription, characterPersonalityTraits, characterBackstory
    return {readyCharacter}
"""
def charGenerator():
    return {
        "name": random.choice(modifiedFileCharName),
        "gender": random.choice(modifiedFileCharGen),
        "age": random.randrange(16, 78),
        "race": random.choice(modifiedFileCharRace),

        "hair": " ".join((
            random.choice(modifiedFileCharHairCol),
            random.choice(modifiedFileCharHairCondAndApp),
            random.choice(modifiedFileCharHairPattern),
            random.choice(modifiedFileCharHairTexture),
        )),

        "eyes": random.choice(modifiedFileCharEyeColor),

        "height": f"Cm: {(h := random.randrange(155, 214))} / Feet: {h / 30.48:.2f}",

        "body": random.choice(modifiedFileCharBodyDes),

        "traits": [
            random.choice(modifiedFileCharPersonalityTraitsPos),
            random.choice(modifiedFileCharPersonalityTraitsPos),
            random.choice(modifiedFileCharPersonalityTraitsPos),
            random.choice(modifiedFileCharPersonalityTraitsNeut),
            random.choice(modifiedFileCharPersonalityTraitsNeut),
            random.choice(modifiedFileCharPersonalityTraitsNeg),
            random.choice(modifiedFileCharPersonalityTraitsNeg),
            random.choice(modifiedFileCharPersonalityTraitsNeg),
        ],

        "backstory": random.choice(modifiedFileCharBackStories),
    }

# __TEST__
print(charGenerator()) 
