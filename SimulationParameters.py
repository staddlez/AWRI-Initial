#################################################################################
# Simulation Parameters Class
#################################################################################
from Fish import Fish


class SimulationParameters:
    parameters: str
    numberTrials: int
    estimatedPopulation: float
    actualPopulation: int
    testData = []
    median: float
    skew: float
    firstQuart: float
    secondQuart: float
    thirdQuart: float
    fourthQuart: float

    # Testing:
    paramCaptureCategory: int
    paramCaptureOne: float
    paramCaptureTwo: float
    paramLowBound: float
    paramHighBound: float
    paramBoundsApply: int

    #################################################################################
    # FISH CONSTRUCTOR
    #################################################################################
    def __init__(self):
        self.numberTrials = -1
        self.estimatedPopulation = -1
        self.actualPopulation = -1
        self.parameters = ''
        self.paramBoundsApply = -1
        self.paramCaptureCategory = -1

    #################################################################################
    # FISH CONSTRUCTOR
    #################################################################################
    def __init__(self, numberTrials: int, estimatedPopulation: float, actualPopulation: int,
                 testData):
        # Trial results:
        self.numberTrials = numberTrials
        self.estimatedPopulation = estimatedPopulation
        self.actualPopulation = actualPopulation
        self.testData = testData
        self.parameters = ''
        self.paramBoundsApply = -1
        self.paramCaptureCategory = -1

    #################################################################################
    # SETTER FOR STRING
    #################################################################################
    def SetParameterString(self, addText):
        self.parameters = self.parameters + addText

    #################################################################################
    # SETTER FOR NUMBER OF TRIALS RAN
    #################################################################################
    def SetNumTrials(self, numTrials):
        self.numberTrials = numTrials

    #################################################################################
    # SETTER FOR OVERALL FISH POPULATION ESTIMATED
    #################################################################################
    def SetOverallEstimatedPopulation(self, estimatedPopulation):
        self.estimatedPopulation = estimatedPopulation

    #################################################################################
    # SETTER FOR ACTUAL FISH POPULATION
    #################################################################################
    def SetActualEstimatedPopulation(self, actualPopulation):
        self.actualPopulation = actualPopulation

    #################################################################################
    # SETTER FOR TEST DATA FOR THIS SIMULATION
    #################################################################################
    def SetActualEstimatedPopulation(self, testData):
        self.testData = testData

    #################################################################################
    # Setter FOR Median
    #################################################################################
    def SetMedian(self, median):
       self.median = median

    #################################################################################
    # SETTER FOR Skewness
    #################################################################################
    def SetSkew(self, skew):
        self.skew = skew

    #################################################################################
    # SETTER FOR first Quartile
    #################################################################################
    def SetFirstQuart(self, firstQuart):
        self.firstQuart = firstQuart

    #################################################################################
    # SETTER FOR second Quartile
    #################################################################################
    def SetSecondQuart(self, secondQuart):
        self.secondQuart = secondQuart

    #################################################################################
    # SETTER FOR third Quartile
    #################################################################################
    def SetThirdQuart(self, thirdQuart):
        self.thirdQuart = thirdQuart

    #################################################################################
    # SETTER FOR fourth Quartile
    #################################################################################
    def SetFourthQuart(self, fourthQuart):
        self.fourthQuart = fourthQuart

    #################################################################################
    # SETTER FOR PARAMETER TESTING CATEGORY
    #################################################################################
    def SetParamCaptureCategory(self, paramCaptureCategory):
        self.paramCaptureCategory = paramCaptureCategory

    #################################################################################
    # SETTER FOR PARAMETER TESTING CAP ONE
    #################################################################################
    def SetParamCaptureOne(self, paramCaptureOne):
        self.paramCaptureOne = paramCaptureOne

    #################################################################################
    # SETTER FOR PARAMETER TESTING CAP TWO
    #################################################################################
    def SetParamCaptureTwo(self, paramCaptureTwo):
        self.paramCaptureTwo = paramCaptureTwo

    #################################################################################
    # SETTER FOR PARAMETER CATEGORY
    #################################################################################
    def SetBoundApplicable(self, paramBoundsApply):
        self.paramBoundsApply = paramBoundsApply

    #################################################################################
    # SETTER FOR PARAMETER TESTING LOW BOUND
    #################################################################################
    def SetParamLowBound(self, paramLowBound):
        self.paramLowBound = paramLowBound

    #################################################################################
    # SETTER FOR PARAMETER TESTING HIGH BOUND
    #################################################################################
    def SetParamHighBound(self, paramHighBound):
        self.paramHighBound = paramHighBound

    #################################################################################
    # GETTER FOR NUMBER OF TRIALS DONE
    #################################################################################
    def GetNumTrials(self):
        return self.numberTrials

    #################################################################################
    # GETTER FOR NUMBER OF TRIALS DONE
    #################################################################################
    def GetOverallEstimatedPopulation(self):
        return self.estimatedPopulation

    #################################################################################
    # GETTER FOR ACTUAL POPULATION
    #################################################################################
    def GetActualPopulation(self):
        return self.actualPopulation

    #################################################################################
    # GETTER FOR NUMBER OF TRIALS DONE
    #################################################################################
    def GetNumTrials(self):
        return self.numberTrials

    #################################################################################
    # GETTER FOR TEST DATA
    #################################################################################
    def GetParameters(self):
        return self.parameters

    #################################################################################
    # GETTER FOR TEST DATA
    #################################################################################
    def GetTestData(self):
        return self.testData

    #################################################################################
    # GETTER FOR Median
    #################################################################################
    def GetMedian(self):
        return self.median

    #################################################################################
    # GETTER FOR Skewness
    #################################################################################
    def GetSkew(self):
        return self.skew

    #################################################################################
    # GETTER FOR first Quartile
    #################################################################################
    def GetFirstQuart(self):
        return self.firstQuart

    #################################################################################
    # GETTER FOR second Quartile
    #################################################################################
    def GetSecondQuart(self):
        return self.secondQuart

    #################################################################################
    # GETTER FOR third Quartile
    #################################################################################
    def GetThirdQuart(self):
        return self.thirdQuart

    #################################################################################
    # GETTER FOR fourth Quartile
    #################################################################################
    def GetFourthQuart(self):
        return self.fourthQuart

    #################################################################################
    # SETTER FOR PARAMETER TESTING CAP ONE
    #################################################################################
    def GetParamCaptureOne(self):
        return self.paramCaptureOne

    #################################################################################
    # SETTER FOR PARAMETER TESTING CAP TWO
    #################################################################################
    def GetParamCaptureTwo(self):
        return self.paramCaptureTwo

    #################################################################################
    # GETTER FOR PARAMETER TESTING CAP ONE
    #################################################################################
    def GetParamCaptureCategory(self):
        return self.paramCaptureCategory

    #################################################################################
    # GETTER FOR PARAMETER TESTING LOW BOUND
    #################################################################################
    def GetParamLowBound(self):
        return self.paramLowBound

    #################################################################################
    # GETTER FOR PARAMETER TESTING HIGH BOUND
    #################################################################################
    def GetParamHighBound(self):
        return self.paramHighBound

    #################################################################################
    # GETTER FOR PARAMETER CATEGORY
    #################################################################################
    def GetBoundApplicable(self):
        return self.paramBoundsApply
