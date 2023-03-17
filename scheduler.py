import numpy as np

print("Hello World")

# ----------------------------ARRAYS--------------------------------------------

chromosomeArray = []

timingsArray = []

coursesArray = []

clashArray = []

hallsArray = []

# ----------------------------CLASSES--------------------------------------------

class timing:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        
class clash:
    def __init__(self, firstCourse, secondCourse):
        self.firstCourse = firstCourse
        self.secondCourse = secondCourse

class course:
    def __init__(self, courseName) -> None:
        self.courseName = courseName
        
class hall:
    def __init__(self, hallName):
        self.hallName = hallName


# ----------------------------FUNCTIONS--------------------------------------------

def createTimings():
    initialTime = 900

    for i in range(0, 9):
        timing.startTime = initialTime + (i * 100)
        timing.endTime = timing.startTime + (100)
        print(timing.startTime)
        print(timing.endTime)
    
    
def checkCommonStudents():
    noMoreStudents = False
    print("Are there any common students :D between courses? Answer with y/n")
    checkMore = input()
    while(noMoreStudents == False):
        while (checkMore != "y" and checkMore != "n"):
            print("Please only enter y/n")
            checkMore = input()
        if (checkMore == "y"):
            print("Enter the first course name")
            courseOne = input()
            print("Enter the second course name")
            courseTwo = input()
            clash.firstCourse = courseOne
            clash.secondCourse = courseTwo
            # countLinkages(courseOne, courseTwo)
            clashArray.append(clash)
            
            #now to check if there are more common students
            
            print("Are there any more common students between courses? Answer with y/n")
            checkAgain = input()
            while (checkAgain != "y" and checkAgain != "n"):
                print("Please only enter y/n")
                checkAgain = input()
            if (checkAgain == "n"):
                noMoreStudents == True
                break
        elif (checkMore == "n"):
            noMoreStudents == True
            break

#basically this is recording the number of clashes for each individial course
#this is also going to return the max number of common links that a course has
    
def countLinkages():
    print("course numbers :" + courseNum)
    numOfClashes = [0] * int(courseNum)
    for i in range(len(clashArray)):
        firstClash = int(clashArray[i].firstCourse[-1])
        secondClash = int(clashArray[i].secondCourse[-1])
        # print("first clash" + firstClash)
        # print("second clash" + secondClash)
        numOfClashes[firstClash] += 1
        numOfClashes[secondClash] += 1
    
    #now to get the maxiumum no of clashes that occured
    
    maxi = 0
    
    for i in range(0, len(numOfClashes)):
        if (numOfClashes[i] > maxi):
            maxi = numOfClashes[i]
    
    return maxi        
    
# ----------------------------INITIALIZATION FUNCTIONS--------------------------------------------

def courseInitialization(courseNum):
    count = 1
    while (count <= courseNum):
        course.courseName = "C" + str(count)
        print(course.courseName)
        coursesArray.append(course)
        count += 1
        
def hallsInitialization(hallNum):
    count = 1
    while (count <= hallNum):
        hall.hallName = "H" + str(count)
        print(hall.hallName)
        hallsArray.append(hall)
        count += 1

# ----------------------------PRE-GENERATION RULE CHECKS--------------------------------------------

def filterData():
    if((hallNum * noTimings) + maxCommonStd >= courseNum):
        chromosomeGeneration()
    else:
        print("The data given cannot be used to generate a schedule")
        print("The number of halls allocated against this number of courses in this schedule is not enough")
        print("Please enter more halls, or lower the number of courses and try again")
        exit()

# ----------------------------CHROMOSOME GENERATION--------------------------------------------

def chromosomeGeneration():
    print("Chromosome generation")

# ----------------------------MAIN FUNCTION--------------------------------------------
        
print("Please enter the number of halls that are available for use")
hallNum = input()

print("Please enter the total number of courses to be arranged in the schedule")
courseNum = input()

noTimings = 9

createTimings()

courseInitialization(int(courseNum))

hallsInitialization(int(hallNum))

checkCommonStudents()

maxCommonStd = countLinkages()

#we need to check the connections of the clashes
#and also need to keep track of the no of clashes that occurs for each course

print("End of Program")

exit()
#now we need the checking function to see if the values given can be used in chormosome generation or not

# def checkingFunction():
    
    


    
    



# creating a chormosome for a tuple having values of exam hall number, time slot, and course name

# chromosomeArray.append((1, 1, "CSE 101"))
