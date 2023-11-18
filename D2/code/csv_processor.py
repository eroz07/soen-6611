import data_validator as data_validator

class CsvProcessor:  
  def __init__(self, file):
    self.file = file

  def read_csv_and_validate(self):
    content = self.file.read() 
    validator = data_validator.DataValidator()
    return validator.process(content)