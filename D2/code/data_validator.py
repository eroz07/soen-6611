import exception.InvalidDataError as InvalidDataError

class DataValidator:
  def __init__(self) -> None:
    pass

  def process(self, str_data):
    return [self.validate(x) for x in str_data.split(',')]
      
  def validate(self, value):
    value = value.strip()
    if not value.isnumeric():
        raise Exception('Invalid data provided - ' + value + '. Please ensure the values provided are integers')
    return int(value)