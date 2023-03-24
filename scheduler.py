import random
import numpy as np

print("Hello World")

# ----------------------------ARRAYS--------------------------------------------

chromosomeArray = []

timingsArray = []

coursesArray = []

clashArray = []

hallsArray = []

scheduleArray = []

# ----------------------------CLASSES--------------------------------------------

class timing:
    def __init__(self, timingName):
        self.timingName = timingName
        
class clash:
    def __init__(self, firstCourse, secondCourse):
        self.firstCourse = firstCourse
        self.secondCourse = secondCourse

class course:
    def __init__(self, courseName):
        self.courseName = courseName
        
class hall:
    def __init__(self, hallName):
        self.hallName = hallName

class chromosome:
    def __init__(self, hall, timing, courseName):
        self.hall = hall
        self.timing = timing
        self.courseName = courseName

class schedule:
    def __init__(self, chromosomeArray2, fitness):
        chromosomeArray2 = list()
        self.chromosomeArray2 = chromosomeArray2
        self.fitness = fitness
        

# ----------------------------FUNCTIONS--------------------------------------------

def createTimings():
    initialTime = 900

    for i in range(0, 9):
        timing.startTime = initialTime + (i * 100)
        timing.endTime = timing.startTime + (100)
    
    
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
    count1 = 0
    while (count1 <= courseNum):
        course1 = course("C" + str(count1 + 1))
        # print(course.courseName) 
        coursesArray.append(course1)
        count1 += 1
                
def hallsInitialization(hallNum):
    count2 = 1
    while (count2 <= hallNum):
        hall2 = hall("H" + str(count2))
        hallsArray.append(hall2)
        count2 += 1

def timeSlotInitialization(noTimings):   
    count3 = 1
    while (count3 <= noTimings):
        timing2 = timing("T" + str(count3))
        timingsArray.append(timing2)
        count3 += 1

#--------------------------------------------PRE-GENERATION RULE CHECKS--------------------------------------------

def filterData():
    if((int(hallNum) * noTimings) + maxCommonStd >= int(courseNum)):
        scheduleGeneration()
    else:
        print("The data given cannot be used to generate a schedule")
        print("The number of halls allocated against this number of courses in this schedule is not enough")
        print("The number of addititional halls required is : " + str((int(hallNum) * noTimings) + maxCommonStd))
        print("Fill in the required number of halls? Answer with y/n")
        checkHallCorrection = input()
        while (checkHallCorrection != "y" and checkHallCorrection != "n"):
            print("Please only enter y/n")
            checkHallCorrection = input()
        if (checkHallCorrection == "y"):
            hallsInitialization((int(hallNum) * noTimings) + maxCommonStd)
            scheduleGeneration()
        elif (checkHallCorrection == "n"):
            exit()
            
# ----------------------------CHROMOSOME GENERATION--------------------------------------------

def chromosomeGeneration(valueGetterSchedule):
    
    valueGetterSchedule.chromosomeArray2 = list()
    
    chromosomeArray1 = list()
   
    for i in range(0, len(coursesArray)):
        chromosome1 = chromosome("", "", "")
        #generating the random numbers for the chromosomes
        randCourse = i #random.randint(0, len(coursesArray) - 1)
        randHall = random.randint(0, len(hallsArray) - 1)
        randTiming = random.randint(0, len(timingsArray) - 1)
        chromosome1.hall = hallsArray[randHall].hallName
        chromosome1.timing = timingsArray[randTiming].timingName
        chromosome1.courseName = coursesArray[randCourse].courseName
        chromosomeArray1.append(chromosome1)
        # chromosome = chromosome("", "", "")
    
    valueGetterSchedule.chromosomeArray2 = chromosomeArray1
    
    return valueGetterSchedule

#basically here we are generating the total schedule using those chromosomes that we just created
        
def scheduleGeneration():
    print("Generating the schedule")
    for i in range(0, 10):
        valueGetterSchedule = schedule([], 0)
        scheduler = chromosomeGeneration(valueGetterSchedule)
        scheduleArray.append(scheduler)
    printSchedule()
    fitnessFunction()


def printSchedule():
    print("The schedule is : ")
    for i in range(0, len(scheduleArray) - 1):
        scheduler2 = schedule([], 0)
        scheduler2.chromosomeArray2 = scheduleArray[i].chromosomeArray2
        for j in range(0, len(scheduler2.chromosomeArray2) - 1):
            print(scheduler2.chromosomeArray2[j].courseName + " " + scheduler2.chromosomeArray2[j].hall + " " + scheduler2.chromosomeArray2[j].timing)
        print(" ")
# ----------------------------FITNESS FUNCTION--------------------------------------------

def fitnessFunction():
    for i in range(0, len(scheduleArray) - 1):
        fitnessValue = 0
        fitnessValue += checkCoursePresence(scheduleArray[i]) #this is going to check if the course is present in the schedule, and if it has appeared more than once in the schedule
        fitnessValue += conditionOne(scheduleArray[i]) #this is going to check if the course has been assigned to the same hall and timing
        # fitnessValue += conditionTwo(scheduleArray[i]) #this is going to check if a course has been assigned more than one time
        # fitnessValue += conditionThree(scheduleArray[i]) #this is going to check 
        scheduleArray[i].fitnessValue = fitnessValue
        print("printing the fitness value")
        print(fitnessValue)

def checkCoursePresence(schedule):
    
    arrayChromo = schedule.chromosomeArray2
    
    fitnessValueCheckingPresence = 0
    
    checkingArray = np.zeros(int(courseNum), dtype=int) #basically making the array to check
  
    for j in range(0, len(arrayChromo) - 1):
        for k in range(0, len(courseNum) - 1):
            if (arrayChromo[j].courseName == coursesArray[k].courseName):
                checkingArray[k] += 1
                fitnessValueCheckingPresence += 1
                if (checkingArray[k] > 1):
                    fitnessValueCheckingPresence += -1
            
        for l in range(0, len(courseNum) - 1):
            if (checkingArray[l] == 0):
                fitnessValueCheckingPresence += -3
    
    return fitnessValueCheckingPresence
    
def conditionOne(schedule):
    
    chromosomeArray = schedule.chromosomeArray2
    
    #checking if the same course has been assigned to the same hall and timing
    fitnessValueConditionOne = 0
    if (len(clashArray) == 0):
        fitnessValueConditionOne += 20
        return fitnessValueConditionOne
    else:
        for i in range(0, len(clashArray) - 1):
            for j in range(0, len(chromosomeArray) - 1):
                if (clashArray[i].firstCourse == chromosomeArray[j].courseName):
                    if (chromosomeArray[j].timing == chromosomeArray[chromosomeArray.index(clashArray[i].secondCourse)].timing):
                        if (chromosomeArray[j].hall == chromosomeArray[chromosomeArray.index(clashArray[i].secondCourse)].hall):
                            fitnessValueConditionOne += -10

    return fitnessValueConditionOne
           
# ----------------------------MAIN FUNCTION--------------------------------------------
        
print("Please enter the number of halls that are available for use")
hallNum = input()

print("Please enter the total number of courses to be arranged in the schedule")
courseNum = input()

noTimings = 9

createTimings()

courseInitialization(int(courseNum))

hallsInitialization(int(hallNum))

timeSlotInitialization(noTimings)

checkCommonStudents()

maxCommonStd = countLinkages()

filterData()

print("End of Program")

exit()