#all functions

# # # # # # # # # # # # # math # # # # # # # # # # # # #
import math
def areaOfTriangle(base, height):
    return (1 / 2) * b * h

def quadraticFormula(a, b, c):
    return [((-1*b)+(math.sqrt(b**2 - 4*a*c)))/(2*a), ((-1*b)-(math.sqrt(b**2 - 4*a*c)))/(2*a)]

def distance(pointA, pointB):
    return math.sqrt(((pointB[0] - pointA[0])**2) + ((pointB[1] - pointA[1])**2))

def midpoint(pointA, pointB):
    return [((pointA[0] + pointB[0]) / 2), ((pointA[1] + pointB[1]) / 2)]

def pyTheoremSolveForHypotenuse(sideA, sideB):
    return math.sqrt(sideA**2 + sideB**2)

def pyTheoremSolveForSide(side, hypotenuse):
    return math.sqrt(hypotenuse**2 - side**2)

def sineLawSolveForSide(degangleA, sidelengthA, degangleB):
    return (sidelengthA/math.sin(math.radians(degangleA)))*(math.sin(math.radians(degangleB)))

def sineLawSolveForAngle(degangleA, sidelengthA, sidelengthB):
    return math.degrees(math.asin(sidelengthB/(sidelengthA/math.sin(math.radians(degangleA)))))

def cosineLawForSide(degangleC, sidelengthA, sidelengthB):
    return math.sqrt(sidelengthA**2 + sidelengthB**2 - (2 * sidelengthA * sidelengthB * math.cos((degangleC*math.pi)/180)))

#finds angle across from sidelength C
def cosineLawForAngle(sidelengthA, sidelengthB, sidelengthC):
    return math.degrees(math.acos((sidelengthA**2 + sidelengthB**2 - sidelengthC**2) / (2 * sidelengthA * sidelengthB)))

# # # # # # # # # # # # # string manipulation # # # # # # # # # # # # #
def removeAllCharacters(string, char):
    i = string.find(char)
    while i != -1:
        string = string[0 : i] + string[i + 1 :]
        i = string.find(char)
    return string

#semi-working multiple splitting
def splitAtMultiple(string, charList):
    for i in range(1, len(charList)):
        string = string.replace(charList[i], charList[0])
    return string.split(charList[0])

#find all indices of a single characters
def findAllIndicesOfMultipleChars(string, charList):
    output = []
    for i in range(len(string)):
        j = 0
        while j < len(charList):
            if string[i] == charList[j]:
                j = len(charList)
                output.append(i)
            else:
                j += 1
    return output

# find the characters that occurs in both substrings
# explore a more efficient algorithm
def findMatchingChars(string1, string2):
    matchingChars = []
    for i in range(len(string1)):
        j = 0
        while j < len(string2):
            if string1[i] == string2[j]:
                matchingChars.append(string1[i])
                j = len(string2)
            else:
                j+=1
    return matchingChars

#returns list of original input values
def removeAllDuplicatesInOrder(list):
    seen = set()
    seen_add = seen.add
    return [x for x in list if not (x in seen or seen_add(x))]
