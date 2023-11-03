from exception.InvalidDataError import InvalidDataError

class Calculator: 
  def __init__(self, data):
    self.data = data

  def set_data(self, data):
    self.data = data
    
  def clear_data(self):
    self.data = None

  def is_data_exists(self):
    if self.data == None or self.data.size == 0:
      raise InvalidDataError()

  def get_min(self):
    self.is_data_exists()
    min = self.data[0]
    for value in self.data:
      if value < min:
        min = value
    return min
  
  def get_max(self):
    self.is_data_exists()
    max = self.data[0]
    for value in self.data:
      if value > max:
        max = value
    return max