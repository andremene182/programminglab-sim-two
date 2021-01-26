class ExamException(Exception):
    pass


class Diff():

  # Class Constructor
  # @param ratio -> rescaling ratio of the diff operation
  #              -> default value = 1
  def __init__(self,ratio=1):


    # Verify if ratio is an int or a float type
    if not (isinstance(ratio, int) or isinstance(ratio,float)):
      raise ExamException('Invalid type for ratio, only int and float supported. Got "{}"'.format(type(ratio)))

    # Verify if ratio is positive
    if (ratio<1):
      raise ExamException('Invalid type for ratio, only int and float supported. Got "{}"'.format(type(ratio)))

    self.ratio = ratio

  # Method compute() 
  # @param numberList -> numeric list to elaborate
  # @returns diffList ->  elaborated list (diff operation with ratio)
  def compute(self,numberList):

    # Verify if numberList is a List type
    if not (isinstance(numberList,list)): 
      raise ExamException('Invalid type for data. Only list supported. Got "{}"'.format(type(numberList)))

   
    # Verify if there are only numeric values in numberList
    for item in numberList:
      if not (isinstance(item, int) or  isinstance(item, float)):
        raise ExamException('Got non-numeric item in the list data: "{}"'.format(item))
    
    # Verify if there are more than 1 values in numberList
    if (len(numberList) < 2):
      raise ExamException('The list is empty or there is only one value.')


    diff = []

    for i,item in enumerate(numberList):
      if not (item == numberList[-1]):
        diffItem = (numberList[i+1]-item)/self.ratio
        diff.append(diffItem)
      else:
        pass

    return diff 