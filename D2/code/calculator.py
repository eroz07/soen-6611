class Calculator: 
  def __init__(self, data):
    self.data = data

  def set_data(self, data):
    self.data = data
    
  def clear_data(self):
    self.data = None

  def is_data_exists(self):
    if self.data == None or len(self.data) == 0:
      raise Exception("No values to calculate")

  # get the min value from dataset
  def get_min(self):
    self.is_data_exists()
    min = self.data[0]
    for value in self.data:
      if value < min:
        min = value
    return min
  
  # get the max value from dataset
  def get_max(self):
    self.is_data_exists()
    max = self.data[0]
    for value in self.data:
      if value > max:
        max = value
    return max
  
  # get the mode (value that appears most frequently) in dataset
  def get_mode(self):
    self.is_data_exists()
    dict = {}
    count, mode = 0, ''
    for item in reversed(self.data):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, mode = dict[item], item
    return str(mode) + ": " + str(count) + " count(s)"
  
  # get the median, if n is:
  # odd: the middle number
  # even: the arithmetic mean of the two middle numbers
  def get_median(self):
    self.is_data_exists()
    mid = int(len(self.data) / 2)
    if (len(self.data) % 2 == 0):
      return (self.data[mid] + self.data[mid - 1]) / 2
    else:
      return self.data[mid]
    
  # get the arithmetic mean of the dataset
  def get_arithmetic_mean(self):
    self.is_data_exists()
    total = 0
    for value in self.data:
      total += value
    return total / len(self.data)
  
  # get the mean absolute deviation (MAD) of the dataset
  def get_mean_abs_deviation(self):
    mean = self.get_arithmetic_mean()
    total = 0
    for value in self.data:
      total += abs(value - mean)
    return total / len(self.data)
  
  # get the standard deviation of the dataset
  def get_standard_deviation(self):
    mean = self.get_arithmetic_mean()
    variance = 0
    for value in self.data:
      variance += (value - mean) ** 2 
    return self.sqrt(variance / len(self.data) - 1)
    
  # uses babylonian method to calculate the square root (approximates a hypotenuse)
  def sqrt(self, value):
    n = 1
    for _ in range(10):
        n = (n + value/n) * 0.5
    return n